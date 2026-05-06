"""
merge_geotiff_density.py
------------------------
Merges multiple GeoTIFF density rasters into one seamless output GeoTIFF
using cosine-feathered weighted blending to eliminate tile boundary artefacts.

Dependencies:
    pip install rasterio numpy scipy

Usage:
    python merge_geotiff_density.py                        # uses INPUT_FILES below
    python merge_geotiff_density.py tile1.tif tile2.tif …  # or pass files as args
"""

import sys
import warnings
import numpy as np
import rasterio
from rasterio.crs import CRS
from rasterio.enums import Resampling
from rasterio.transform import from_bounds
from rasterio.warp import calculate_default_transform, reproject
from rasterio.merge import merge as rio_merge

# ──────────────────────────────────────────────────────────────────────────────
# CONFIG  –  edit these if you run the script without CLI arguments
# ──────────────────────────────────────────────────────────────────────────────

INPUT_FILES = [
    "tile_1.tif",
    "tile_2.tif",
    "tile_3.tif",
    "tile_4.tif",
    "tile_5.tif",
    "tile_6.tif",
]

OUTPUT_FILE  = "merged_density.tif"

# Fraction of each tile edge used for the cosine fade (0.15 = 15 % on each side).
# Increase to 0.25–0.35 if seams are still visible.
FEATHER      = 0.20

# Target CRS (EPSG code).  Set to None to reuse the CRS of the first tile.
TARGET_EPSG  = None   # e.g. 4326 for WGS-84, 3857 for Web Mercator

# ──────────────────────────────────────────────────────────────────────────────


def cosine_weight_mask(h: int, w: int, feather: float) -> np.ndarray:
    """
    Returns a (h, w) float32 array with 1.0 in the centre and a smooth
    cosine fade to 0.0 at all four edges.
    """
    def ramp(n, frac):
        f = max(1, int(n * frac))
        v = np.ones(n, dtype=np.float32)
        fade = 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, f))
        v[:f]  = fade
        v[-f:] = fade[::-1]
        return v

    return ramp(h, feather)[:, None] * ramp(w, feather)[None, :]


def reproject_to_crs(src, target_crs):
    """Reproject an open rasterio dataset to target_crs; returns (data, transform)."""
    transform, width, height = calculate_default_transform(
        src.crs, target_crs, src.width, src.height, *src.bounds
    )
    data = np.zeros((src.count, height, width), dtype=np.float32)
    for band in range(1, src.count + 1):
        reproject(
            source=rasterio.band(src, band),
            destination=data[band - 1],
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=transform,
            dst_crs=target_crs,
            resampling=Resampling.bilinear,
        )
    return data, transform


def merge_density_geotiffs(
    input_files: list[str],
    output_file: str,
    feather: float = 0.20,
    target_epsg: int | None = None,
) -> None:
    """
    Parameters
    ----------
    input_files  : list of GeoTIFF paths.
    output_file  : path for the merged output GeoTIFF.
    feather      : cosine fade fraction (0–0.5).
    target_epsg  : reproject everything to this EPSG before merging.
                   Pass None to use the CRS of the first tile.
    """
    if not input_files:
        raise ValueError("No input files provided.")

    print(f"Opening {len(input_files)} tiles …")
    sources = [rasterio.open(p) for p in input_files]

    # ── 1. Determine target CRS ──────────────────────────────────────────────
    target_crs = CRS.from_epsg(target_epsg) if target_epsg else sources[0].crs
    print(f"Target CRS: {target_crs.to_string()}")

    # ── 2. Use rasterio.merge to build a common canvas & pixel grid ──────────
    #    (method='first' is irrelevant here; we replace the data ourselves)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        canvas, canvas_transform = rio_merge(
            sources,
            method="first",
            resampling=Resampling.bilinear,
            target_aligned_pixels=True,
            nodata=0,
        )

    n_bands, H, W = canvas.shape
    print(f"Canvas size: {W} × {H} px, {n_bands} band(s)")

    accum  = np.zeros((n_bands, H, W), dtype=np.float64)
    weight = np.zeros((H, W),          dtype=np.float64)

    # ── 3. Reproject each tile onto the canvas and accumulate ────────────────
    for i, (src, path) in enumerate(zip(sources, input_files)):
        print(f"  Processing tile {i+1}/{len(input_files)}: {path}")

        # Reproject tile data onto canvas grid
        tile_data = np.zeros((n_bands, H, W), dtype=np.float32)
        tile_mask = np.zeros((H, W), dtype=np.float32)   # 1 where tile covers

        for band in range(1, n_bands + 1):
            reproject(
                source=rasterio.band(src, band),
                destination=tile_data[band - 1],
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=canvas_transform,
                dst_crs=target_crs,
                dst_nodata=0,
                resampling=Resampling.bilinear,
            )

        # Coverage mask: pixels this tile actually fills (non-nodata)
        nodata = src.nodata if src.nodata is not None else 0
        covered = np.any(tile_data != nodata, axis=0).astype(np.float32)

        # Find bounding box of covered pixels for the feather mask
        rows = np.where(covered.any(axis=1))[0]
        cols = np.where(covered.any(axis=0))[0]
        if rows.size == 0 or cols.size == 0:
            print(f"    ⚠  Tile {i+1} has no coverage on canvas, skipping.")
            continue

        r0, r1 = rows[0], rows[-1] + 1
        c0, c1 = cols[0], cols[-1] + 1
        th, tw = r1 - r0, c1 - c0

        # Cosine weight mask sized to the tile's footprint
        local_mask = cosine_weight_mask(th, tw, feather)

        # Place it on the full canvas (zero outside the tile's footprint)
        full_mask = np.zeros((H, W), dtype=np.float32)
        full_mask[r0:r1, c0:c1] = local_mask

        # Only weight pixels that are actually covered (not nodata)
        full_mask *= covered

        for band in range(n_bands):
            accum[band] += tile_data[band] * full_mask

        weight += full_mask

    src.close()
    for s in sources:
        s.close()

    # ── 4. Normalise ─────────────────────────────────────────────────────────
    with np.errstate(invalid="ignore", divide="ignore"):
        merged = np.where(weight > 0, accum / weight, 0).astype(np.float32)

    print("Blending complete.")

    # ── 5. Write output GeoTIFF ──────────────────────────────────────────────
    profile = sources[0].profile.copy()
    profile.update(
        driver     = "GTiff",
        height     = H,
        width      = W,
        count      = n_bands,
        dtype      = "float32",
        crs        = target_crs,
        transform  = canvas_transform,
        nodata     = 0,
        compress   = "lzw",
        tiled      = True,
        blockxsize = 256,
        blockysize = 256,
    )

    with rasterio.open(output_file, "w", **profile) as dst:
        dst.write(merged)

    print(f"\n✓ Merged GeoTIFF saved to: {output_file}")
    print(f"  Size : {W} × {H} px")
    print(f"  Bands: {n_bands}")
    print(f"  CRS  : {target_crs.to_string()}")
    bounds = rasterio.transform.array_bounds(H, W, canvas_transform)
    print(f"  Bounds (xmin ymin xmax ymax): {[round(b, 6) for b in bounds]}")


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    files = sys.argv[1:] if len(sys.argv) > 1 else INPUT_FILES
    merge_density_geotiffs(
        input_files  = files,
        output_file  = OUTPUT_FILE,
        feather      = FEATHER,
        target_epsg  = TARGET_EPSG,
    )

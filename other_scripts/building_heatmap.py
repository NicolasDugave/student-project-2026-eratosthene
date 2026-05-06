"""
building_heatmap.py
===================
Génère une heatmap de densité du bâti à partir d'une ortophoto géoréférencée (.tif).

Pipeline :
  1. Lecture du .tif (rasterio) → conservation de la projection et du geotransform
  2. Détection des pixels sombres/gris (bâti) via espace HSV
  3. Suppression des structures linéaires (routes) par analyse d'excentricité
  4. Filtre médian pour homogénéiser le masque
  5. Flou gaussien pour estimer la densité
  6. Export en .tif géoréférencé (Float32, valeurs 0–1)

Dépendances :
    pip install rasterio numpy scipy scikit-image

Utilisation :
    python building_heatmap.py --input photo.tif --output heatmap.tif

    # Avec paramètres personnalisés :
    python building_heatmap.py \\
        --input photo.tif \\
        --output heatmap.tif \\
        --brightness 110 \\
        --saturation 45 \\
        --min-area 80 \\
        --max-eccentricity 0.96 \\
        --median-size 7 \\
        --gaussian-sigma 40 \\
        --debug
"""

import argparse
import sys
import time
from pathlib import Path

import numpy as np
import rasterio
from rasterio.enums import Resampling
import scipy.ndimage as ndi
from scipy.ndimage import median_filter
from skimage import morphology, measure
from skimage.color import rgb2hsv


# ─────────────────────────────────────────────────────────────────────────────
# 1. LECTURE DE L'IMAGE
# ─────────────────────────────────────────────────────────────────────────────

def load_tif(path: str):
    """
    Charge un .tif géoréférencé et retourne :
      - img_rgb  : array (H, W, 3) uint8
      - profile  : métadonnées rasterio (CRS, transform, etc.)
      - nodata_mask : masque booléen True = pixel invalide (nodata)
    """
    print(f"[1/5] Lecture de {path} ...")
    with rasterio.open(path) as src:
        profile = src.profile.copy()
        count   = src.count

        if count < 3:
            sys.exit(f"Erreur : l'image doit avoir au moins 3 bandes (R,G,B). Bandes trouvées : {count}")

        # Lecture des 3 premières bandes (R, G, B)
        r = src.read(1)
        g = src.read(2)
        b = src.read(3)

        # Masque nodata (True = invalide)
        nodata = src.nodata
        if nodata is not None:
            nodata_mask = (r == nodata) | (g == nodata) | (b == nodata)
        else:
            nodata_mask = np.zeros(r.shape, dtype=bool)

    # Normalisation en uint8 si nécessaire (ex. uint16)
    def to_uint8(band):
        if band.dtype == np.uint8:
            return band
        vmin, vmax = np.percentile(band[~nodata_mask], (1, 99)) if nodata_mask.any() else np.percentile(band, (1, 99))
        band = np.clip((band.astype(float) - vmin) / (vmax - vmin + 1e-6) * 255, 0, 255)
        return band.astype(np.uint8)

    img_rgb = np.stack([to_uint8(r), to_uint8(g), to_uint8(b)], axis=-1)
    print(f"    Dimensions : {img_rgb.shape[1]} x {img_rgb.shape[0]} px  |  CRS : {profile.get('crs')}")
    return img_rgb, profile, nodata_mask


def local_normalize(img_rgb, radius=200):
    """
    Normalisation locale : corrige les gradients d'éclairage (vignettage, plis…).

    Pour chaque canal :
      1. Estime le fond lumineux via un grand flou gaussien (σ = radius px)
      2. Divise le pixel par le fond  →  valeur relative, indépendante du niveau global
      3. Remet à l'échelle [0, 255] uint8

    radius : doit être >> taille d'un bâtiment, mais << taille du gradient d'éclairage.
             Typiquement 150–300 px pour des cartes 300 dpi.
    """
    print(f"[1b/5] Normalisation locale (σ={radius}px) — correction vignettage ...")
    out = np.zeros_like(img_rgb, dtype=np.float32)

    for i in range(3):
        channel = img_rgb[:, :, i].astype(np.float32)
        # Fond lumineux = basse fréquence spatiale
        background = ndi.gaussian_filter(channel, sigma=radius)
        # Division par le fond (éviter /0)
        normalized = channel / (background + 1e-6)
        # Remettre à l'échelle : percentiles robustes → [0, 255]
        p1, p99 = np.percentile(normalized, (1, 99))
        normalized = np.clip((normalized - p1) / (p99 - p1 + 1e-6) * 255, 0, 255)
        out[:, :, i] = normalized

    return out.astype(np.uint8)



# Presets HSV — toutes les valeurs sont en [0, 1]
#   H : teinte   0/1=rouge, 0.08=jaune, 0.33=vert, 0.5=cyan, 0.67=bleu, 0.83=magenta
#   S : saturation  0=gris pur, 1=couleur pure
#   V : luminosité  0=noir, 1=blanc
# Format : (H_min, H_max, S_min, S_max, V_min, V_max)
# Le rouge "wrape" autour de 0/1 : H_min > H_max est géré par _hue_in_range.

PRESETS = {
    "dark":      (0.0,  1.0,  0.0,  0.45, 0.0,  0.42),  # noir / gris foncé
    "lightgray": (0.0,  1.0,  0.0,  0.15, 0.45, 0.82),  # gris clair
    "red":       (0.93, 0.08, 0.35, 1.0,  0.35, 1.0 ),  # rouge vif (cadastre)
    "pink":      (0.88, 0.05, 0.15, 0.75, 0.55, 1.0 ),  # rose pâle
    "brown":     (0.04, 0.12, 0.25, 0.75, 0.25, 0.72),  # brun / ocre
    "blue":      (0.55, 0.70, 0.25, 1.0,  0.20, 0.85),  # bleu
    "green":     (0.25, 0.45, 0.20, 1.0,  0.15, 0.75),  # vert
}


def _hue_in_range(H, h_min, h_max):
    """Gère le wrap circulaire de la teinte (ex. rouge : 0.93 → 0.08)."""
    if h_min <= h_max:
        return (H >= h_min) & (H <= h_max)
    return (H >= h_min) | (H <= h_max)  # wrap autour de 0


def detect_buildings(img_rgb, nodata_mask,
                     preset=None,
                     h_min=None, h_max=None,
                     s_min=None, s_max=None,
                     v_min=None, v_max=None):
    """
    Détecte les pixels de bâti selon une ou plusieurs plages HSV.

    `preset` peut être :
      - une chaîne simple  : "dark"
      - plusieurs presets séparés par "+" : "dark+red"  → union des masques (OR)

    Tout override individuel (--h-min…) s'applique uniquement au PREMIER preset.

    Retourne un masque binaire uint8 (1 = bâti candidat).
    """
    hsv = rgb2hsv(img_rgb)
    H, S, V = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]

    preset_list = [p.strip() for p in (preset or "dark").split("+")]
    combined = np.zeros(img_rgb.shape[:2], dtype=bool)

    for idx, pname in enumerate(preset_list):
        base = PRESETS.get(pname, PRESETS["dark"])
        ph_min, ph_max, ps_min, ps_max, pv_min, pv_max = base

        # Les overrides CLI ne s'appliquent qu'au premier preset
        if idx == 0:
            H_min = h_min if h_min is not None else ph_min
            H_max = h_max if h_max is not None else ph_max
            S_min = s_min if s_min is not None else ps_min
            S_max = s_max if s_max is not None else ps_max
            V_min = v_min if v_min is not None else pv_min
            V_max = v_max if v_max is not None else pv_max
        else:
            H_min, H_max = ph_min, ph_max
            S_min, S_max = ps_min, ps_max
            V_min, V_max = pv_min, pv_max

        layer = (
            _hue_in_range(H, H_min, H_max) &
            (S >= S_min) & (S <= S_max) &
            (V >= V_min) & (V <= V_max) &
            (~nodata_mask)
        )
        pct = layer.sum() / layer.size * 100
        print(f"[2/5] Preset '{pname}' : {layer.sum():,} px ({pct:.1f}%)"
              f"  H∈[{H_min:.2f},{H_max:.2f}] S∈[{S_min:.2f},{S_max:.2f}] V∈[{V_min:.2f},{V_max:.2f}]")
        combined |= layer

    mask = combined.astype(np.uint8)
    pct_total = mask.sum() / mask.size * 100
    if len(preset_list) > 1:
        print(f"    Union ({'+'.join(preset_list)}) : {mask.sum():,} px ({pct_total:.1f}%)")
    return mask


# ─────────────────────────────────────────────────────────────────────────────
# 3. SUPPRESSION DES ROUTES (structures linéaires)
# ─────────────────────────────────────────────────────────────────────────────

def remove_roads(binary_mask, min_area, max_eccentricity, closing_radius):
    """
    Supprime les composantes connexes très allongées (routes, fossés…).

    Principe :
      - L'excentricité d'une ellipse ajustée à la composante vaut 0 pour un cercle
        et tend vers 1 pour une ligne parfaite.
      - On conserve les composantes dont l'excentricité < max_eccentricity
        (formes compactes = bâtiments) et l'aire >= min_area.

    Paramètres :
      closing_radius  : rayon (px) du disque de fermeture morphologique appliqué
                        avant le labeling (pour combler les petits trous dans les toits).
    """
    print(f"[3/5] Suppression des routes (excentricité > {max_eccentricity}, aire < {min_area} px) ...")

    # Fermeture morphologique : unit les fragments de bâtiments proches
    closed = morphology.binary_closing(binary_mask.astype(bool), morphology.disk(closing_radius))

    # Étiquetage des composantes connexes
    labeled = measure.label(closed, connectivity=2)
    props   = measure.regionprops(labeled)

    building_mask = np.zeros_like(binary_mask, dtype=np.uint8)
    kept = 0

    for prop in props:
        # Filtre 1 : aire minimale (élimine le bruit)
        if prop.area < min_area:
            continue
        # Filtre 2 : excentricité (élimine les lignes = routes)
        #   Note : excentricité = None pour les composantes d'1 pixel → on ignore
        if prop.eccentricity is None or prop.eccentricity >= max_eccentricity:
            continue
        building_mask[labeled == prop.label] = 1
        kept += 1

    print(f"    Composantes conservées (bâtiments) : {kept}")
    return building_mask


# ─────────────────────────────────────────────────────────────────────────────
# 4 & 5. FILTRE MÉDIAN + FLOU GAUSSIEN → HEATMAP
# ─────────────────────────────────────────────────────────────────────────────

def create_heatmap(building_mask, median_size, gaussian_sigma, mode="count"):
    """
    Deux modes de pondération :

    - mode="area"  (ancien comportement) : floute le masque binaire brut.
                   Les grands bâtiments dominent car ils ont plus de pixels.

    - mode="count" (recommandé) : place 1 point au centroïde de chaque bâtiment,
                   puis floute. Grand ou petit, chaque bâtiment pèse exactement 1.
                   Révèle la densité de bâtiments plutôt que leur surface cumulée.

    Retourne un array float32 normalisé en [0, 1].
    """
    print(f"[4/5] Mode '{mode}' | Médian (kernel={median_size}px) + Gaussien (σ={gaussian_sigma}px) ...")

    if mode == "count":
        # ── Mode centroïde : 1 bâtiment = 1 point, quelle que soit sa taille ──
        labeled = measure.label(building_mask, connectivity=2)
        props   = measure.regionprops(labeled)

        point_map = np.zeros(building_mask.shape, dtype=np.float32)
        for prop in props:
            cy, cx = int(round(prop.centroid[0])), int(round(prop.centroid[1]))
            cy = np.clip(cy, 0, point_map.shape[0] - 1)
            cx = np.clip(cx, 0, point_map.shape[1] - 1)
            point_map[cy, cx] = 1.0

        print(f"    Bâtiments comptés (centroïdes) : {int(point_map.sum()):,}")

        # !! Gaussien EN PREMIER sur les points isolés :
        #    le médian sur une carte quasi-vide retourne 0 partout → image noire
        heatmap = ndi.gaussian_filter(point_map, sigma=gaussian_sigma)

        # Médian ensuite, sur la carte déjà étalée
        heatmap = median_filter(heatmap, size=median_size)

    else:
        # ── Mode area : pondération par surface (biais grands bâtiments) ──
        smoothed = median_filter(building_mask.astype(np.float32), size=median_size)
        heatmap = ndi.gaussian_filter(smoothed, sigma=gaussian_sigma)

    # Normalisation 0–1
    hmax = heatmap.max()
    if hmax > 0:
        heatmap /= hmax
    else:
        print("    ⚠ Heatmap entièrement nulle — vérifiez les seuils de détection ou lancez --debug")

    return heatmap.astype(np.float32)


# ─────────────────────────────────────────────────────────────────────────────
# 6. EXPORT EN .TIF GÉORÉFÉRENCÉ
# ─────────────────────────────────────────────────────────────────────────────

def save_tif(heatmap, profile, output_path, debug_masks=None):
    """
    Sauvegarde la heatmap en Float32 géoréférencé.
    Si debug_masks est fourni, sauvegarde aussi les masques intermédiaires.
    """
    print(f"[5/5] Export → {output_path} ...")

    out_profile = profile.copy()
    out_profile.update({
        "count":   1,
        "dtype":   "float32",
        "nodata":  -1.0,
        "compress": "lzw",
        "photometric": "MINISBLACK",
    })
    # Supprimer les clés incompatibles mono-bande
    for key in ("photometric",):
        out_profile.pop(key, None)

    with rasterio.open(output_path, "w", **out_profile) as dst:
        dst.write(heatmap, 1)
        dst.update_tags(
            DESCRIPTION="Heatmap densité bâti — valeurs 0 (vide) à 1 (dense)"
        )

    print(f"    ✓ Heatmap enregistrée : {output_path}")

    # Fichiers de debug (masques intermédiaires en uint8)
    if debug_masks:
        debug_profile = profile.copy()
        debug_profile.update({"count": 1, "dtype": "uint8", "nodata": 255})

        for name, mask in debug_masks.items():
            dp = Path(output_path).with_name(f"debug_{name}.tif")
            with rasterio.open(str(dp), "w", **debug_profile) as dst:
                dst.write(mask.astype(np.uint8), 1)
            print(f"    ✓ Debug '{name}' → {dp}")


# ─────────────────────────────────────────────────────────────────────────────
# POINT D'ENTRÉE
# ─────────────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(
        description="Heatmap densité bâti depuis un .tif géoréférencé",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--input",  "-i", required=True,  help="Chemin vers le .tif source")
    p.add_argument("--output", "-o", required=True,  help="Chemin vers le .tif de sortie")

    p.add_argument("--local-norm", action="store_true",
                   help="Active la normalisation locale (recommandé si éclairage non homogène / vignettage)")
    p.add_argument("--local-norm-radius", type=int, default=200,
                   help="Rayon (px) du flou estimant le fond lumineux. "
                        "Doit être >> taille d'un bâtiment (défaut: 200)")

    # Détection — preset + overrides fins
    preset_names = ", ".join(PRESETS.keys())
    p.add_argument("--preset", default="dark",
                   help=f"Couleur(s) du bâti. Un preset ou plusieurs séparés par '+'. "
                        f"Ex: 'dark+red' pour détecter gris ET rouge. "
                        f"Valeurs disponibles : {preset_names}")
    p.add_argument("--h-min", type=float, default=None,
                   help="Override : teinte min HSV [0–1] (écrase le preset)")
    p.add_argument("--h-max", type=float, default=None,
                   help="Override : teinte max HSV [0–1]")
    p.add_argument("--s-min", type=float, default=None,
                   help="Override : saturation min [0–1]")
    p.add_argument("--s-max", type=float, default=None,
                   help="Override : saturation max [0–1]")
    p.add_argument("--v-min", type=float, default=None,
                   help="Override : luminosité min [0–1]")
    p.add_argument("--v-max", type=float, default=None,
                   help="Override : luminosité max [0–1]")

    # Suppression des routes
    p.add_argument("--min-area",         type=int,   default=60,
                   help="Aire minimale (px²) d'une composante pour être considérée bâtiment")
    p.add_argument("--max-eccentricity", type=float, default=0.97,
                   help="Excentricité max (0=cercle, 1=ligne) : au-delà → supprimé (route)")
    p.add_argument("--closing-radius",   type=int,   default=3,
                   help="Rayon (px) de la fermeture morphologique avant labeling")

    # Lissage
    p.add_argument("--median-size",    type=int,   default=5,
                   help="Taille du noyau du filtre médian (px, nombre impair)")
    p.add_argument("--gaussian-sigma", type=float, default=30,
                   help="Écart-type (px) du flou gaussien pour la densité")

    p.add_argument("--mode", choices=["count", "area"], default="count",
                   help="'count' = 1 point/bâtiment (recommandé, sans biais de taille) | "
                        "'area' = pondération par surface (ancien comportement)")
    p.add_argument("--debug", action="store_true",
                   help="Enregistre les masques intermédiaires (debug_*.tif)")
    return p.parse_args()


def main():
    args = parse_args()
    t0 = time.time()

    # Vérifications
    if not Path(args.input).exists():
        sys.exit(f"Erreur : fichier introuvable → {args.input}")

    # Pipeline
    img_rgb, profile, nodata_mask = load_tif(args.input)

    if args.local_norm:
        img_rgb = local_normalize(img_rgb, radius=args.local_norm_radius)

    raw_mask = detect_buildings(
        img_rgb,
        nodata_mask=nodata_mask,
        preset=args.preset,
        h_min=args.h_min, h_max=args.h_max,
        s_min=args.s_min, s_max=args.s_max,
        v_min=args.v_min, v_max=args.v_max,
    )

    building_mask = remove_roads(
        raw_mask,
        min_area=args.min_area,
        max_eccentricity=args.max_eccentricity,
        closing_radius=args.closing_radius,
    )

    heatmap = create_heatmap(
        building_mask,
        median_size=args.median_size,
        gaussian_sigma=args.gaussian_sigma,
        mode=args.mode,
    )

    debug_masks = None
    if args.debug:
        debug_masks = {
            "1_raw_detection": raw_mask,
            "2_after_road_removal": building_mask,
        }

    save_tif(heatmap, profile, args.output, debug_masks=debug_masks)

    print(f"\nTerminé en {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
---
layout: default
---

<style>
  @import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Yeseva+One&display=swap");

  .tm-container {
    width: 90vw !important;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-direction: column;
  }

  #map {
    position: relative;
    height: 600px;
    width: 100%;
  }

  #year-slider {
    -webkit-appearance: none;
    width: 100%;
    background: #3f3f46;
    height: 12px;
    border-radius: 999px;
    outline: none;
    margin: 0;
    padding: 0;
    cursor: pointer;
  }

  .slider-label-container {
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding: 0 16px;
    margin-top: 1.5rem;
    box-sizing: border-box;
  }
/* 
  .leaflet-control-layers {
    border: 0;
    border-radius: 0.75rem;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
    overflow: visible;
    position: relative;
    z-index: 1200;
    pointer-events: auto;
  }

  .leaflet-control-container {
    z-index: 1200;
    pointer-events: auto;
  } */
</style>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.8.0/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.8.0/dist/leaflet.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.9.2/proj4.js"></script>
<script src="https://cdn.tailwindcss.com"></script>

<script>
  tailwind.config = {
    theme: {
      fontFamily: {
        sans: "Poppins",
        serif: "IBM Plex Serif",
      },
    },
  };
</script>

<div class="tm-container bg-zinc-800" id="top-of-page">
  
  <div class="px-8 py-6 flex justify-between items-center text-white border-b border-zinc-700">
    <div class="w-1/3">
      <h1 id="date-text" class="text-7xl font-thin">1907</h1>
    </div>
    <div class="text-right">
      <h2 class="text-4xl md:text-5xl italic font-black">Lausanne Time Machine</h2>
      <p class="text-sm font-light not-italic">
        Une histoire géographique du développement des transports publics dans le centre ville de Lausanne.
      </p>
    </div>
  </div>

  <div id="map" class="bg-black"></div>

<div class="py-12 bg-zinc-900 w-full">
    <div class="w-11/12 md:w-5/6 mx-auto relative px-0"> 
      <input 
        type="range" 
        id="year-slider" 
        min="0" 
        max="6" 
        step="1" 
        value="0"
      >
      <div class="slider-label-container text-zinc-400 text-sm md:text-2xl font-black">
        <span class="w-0 flex justify-center whitespace-nowrap">1907</span>
        <span class="w-0 flex justify-center whitespace-nowrap">1925</span>
        <span class="w-0 flex justify-center whitespace-nowrap">1937</span>
        <span class="w-0 flex justify-center whitespace-nowrap">1973</span>
        <span class="w-0 flex justify-center whitespace-nowrap">1983</span>
        <span class="w-0 flex justify-center whitespace-nowrap">2000</span>
        <span class="w-0 flex justify-center whitespace-nowrap">2025</span>
      </div>
    </div>
  </div>
</div>

<a href="#top-of-page" id="back-to-top" class="fixed right-10 bottom-10 hidden z-50 bg-white rounded-full p-2 shadow-2xl">
  <svg width="40" height="40" viewBox="0 0 100 100">
    <path fill="black" d="m50 0c-13.262 0-25.98 5.2695-35.355 14.645s-14.645 22.094-14.645 35.355 5.2695 25.98 14.645 35.355 22.094 14.645 35.355 14.645 25.98-5.2695 35.355-14.645 14.645-22.094 14.645-35.355-5.2695-25.98-14.645-35.355-22.094-14.645-35.355-14.645zm20.832 62.5-20.832-22.457-20.625 22.457c-1.207 0.74219-2.7656 0.57812-3.7891-0.39844-1.0273-0.98047-1.2695-2.5273-0.58594-3.7695l22.918-25c0.60156-0.61328 1.4297-0.96094 2.2891-0.96094 0.86328 0 1.6914 0.34766 2.293 0.96094l22.918 25c0.88672 1.2891 0.6875 3.0352-0.47266 4.0898-1.1562 1.0508-2.9141 1.0859-4.1133 0.078125z"></path>
  </svg>
</a>

<script>
  (async () => {
    const yearSteps = [1907, 1925, 1937, 1973, 1983, 2000, 2025];
    const transportDefinitions = {
      1907: [
        {
          url: "/_file/data/trans_1907/1907_tram.geojson",
          color: "#b2df8a",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          url: "/_file/data/trans_1907/1907_funiculaire.geojson",
          color: "#fb9a99",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/trans_1907/1907_train.geojson",
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/limits/1907_lim.geojson",
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      1925: [
        {
          url: "/_file/data/trans_1925/1925_bus.geojson",
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          url: "/_file/data/trans_1925/1925_tram.geojson",
          color: "#b2df8a",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          url: "/_file/data/trans_1925/1925_funiculaire.geojson",
          color: "#fb9a99",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/trans_1925/1925_train.geojson",
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/limits/1925_lim.geojson",
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      1937: [
        {
          url: "/_file/data/trans_1937/1937_tram.geojson",
          color: "#b2df8a",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          url: "/_file/data/trans_1937/1937_funiculaire.geojson",
          color: "#fb9a99",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/trans_1937/1937_train.geojson",
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/limits/1937_lim.geojson",
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      1973: [
        {
          url: "/_file/data/trans_1973/1973_busv3.geojson",
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          url: "/_file/data/trans_1973/1973_funi.geojson",
          color: "#fb9a99",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/trans_1973/1973_ferv2.geojson",
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/limits/1973_lim.geojson",
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      1983: [
        {
          url: "/_file/data/trans_1983/rout_ligne_v2.geojson",
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          url: "/_file/data/trans_1983/funiculaire.geojson",
          color: "#fb9a99",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/trans_1983/ferroviaire_v2.geojson",
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/limits/1983_lim.geojson",
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      2000: [
        {
          url: "/_file/data/trans_2000/ROUTE_ligne_2000.geojson",
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          url: "/_file/data/trans_2000/FUNI_ligne_2000.geojson",
          color: "#fb9a99",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/trans_2000/FER_ligne_2000.geojson",
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
        {
          url: "/_file/data/limits/2000_lim.geojson",
          color: "#000000",
          weight: 4,
          opacity: 1,
        },
      ],
      2025: [
        {
          url: "/_file/data/trans_2025/ROUTE_ligne_2025.geojson",
          color: "#1f78b4",
          weight: 2.5,
          opacity: 0.9,
        },
        {
          url: "/_file/data/trans_2025/FER_ligne_2025.geojson",
          color: "#e31a1c",
          weight: 3.2,
          opacity: 1,
        },
      ],
    };

    const slider = document.getElementById("year-slider");
    const dateText = document.getElementById("date-text");
    const backToTop = document.getElementById("back-to-top");

    const map = L.map("map", {
      minZoom: 12,
      maxZoom: 16,
      maxBounds: [
        [46.48743, 6.51906],
        [46.68011, 6.74191],
      ],
      maxBoundsViscosity: 1,
    }).setView([46.519, 6.633], 13);

    map.createPane("transportPane");
    map.getPane("transportPane").style.zIndex = 650;

    // map.createPane("overlayPane");
    // map.getPane("overlayPane").style.zIndex = 500;

    // map.createPane("limitsPane");
    // map.getPane("limitsPane").style.zIndex = 700;

    L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png", {
      attribution: "&copy; OpenStreetMap",
    }).addTo(map);

    // const transparentTileUrl = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIW2NgYGD4DwABBAEAffm4LQAAAABJRU5ErkJggg==";



    // const overlayLayerTemplates = {
    //   "Historical map": {
    //     1907: "/_file/data/tiles_1907/{z}/{x}/{y}.png",
    //     1925: "/_file/data/tiles_1925/{z}/{x}/{y}.png",
    //     1937: "/_file/data/tiles_1937/{z}/{x}/{y}.png",
    //     1973: "/_file/data/tiles_1973/{z}/{x}/{y}.png",
    //     1983: "/_file/data/tiles_1983/{z}/{x}/{y}.png",
    //     2000: "/_file/data/tiles_2000/{z}/{x}/{y}.png",
    //     // 2025: "/_file/data/tiles_1925/{z}/{x}/{y}.png",
    //   },
    //   "Density": {
    //     1907: "/_file/data/heatmap_1907/{z}/{x}/{y}.png",
    //     1925: "/_file/data/heatmap_1925/{z}/{x}/{y}.png",
    //     1937: "/_file/data/heatmap_1937/{z}/{x}/{y}.png",
    //     1973: "/_file/data/heatmap_1973/{z}/{x}/{y}.png",
    //     1983: "/_file/data/heatmap_1983/{z}/{x}/{y}.png",
    //     2000: "/_file/data/heatmap_2000/{z}/{x}/{y}.png",
    //     2025: "/_file/data/heatmap_1925/{z}/{x}/{y}.png",
    //   },
    // };

    // const limitsLayerUrls = {
    //   // 1907: "/_file/data/limits/limits_1907.geojson",
    //   1925: "/_file/data/limits/1925_lim.geojson",
    //   // 1937: "/_file/data/limits/limits_1937.geojson",
    //   // 1973: "/_file/data/limits/limits_1973.geojson",
    //   // 1983: "/_file/data/limits/limits_1983.geojson",
    //   // 2000: "/_file/data/limits/limits_2000.geojson",
    //   // 2025: "/_file/data/limits/limits_2025.geojson",
    // };

    // const overlayLayers = {
    //   "Historical map": L.tileLayer(transparentTileUrl, {
    //     pane: "overlayPane",
    //     opacity: 0.7,
    //     attribution: "Archives de Lausanne",
    //     minZoom: 12,
    //     maxZoom: 16,
    //   }),
    //   "Density": L.tileLayer(transparentTileUrl, {
    //     pane: "overlayPane",
    //     opacity: 0.7,
    //     attribution: "Archives de Lausanne",
    //     minZoom: 12,
    //     maxZoom: 16,
    //   }),
    //   "Limits": L.layerGroup(),
    // };

    // const overlayControl = L.control.layers({}, overlayLayers, {
    //   collapsed: false,
    // }).addTo(map);

    // proj4.defs(
    //   "EPSG:2056",
    //   "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs"
    // );

    // function reprojectCoordinateArray(coords) {
    //   if (!Array.isArray(coords) || coords.length === 0) return coords;
    //   if (typeof coords[0] === "number") {
    //     const [lng, lat] = proj4("EPSG:2056", "EPSG:4326", [coords[0], coords[1]]);
    //     return [lng, lat];
    //   }
    //   return coords.map(reprojectCoordinateArray);
    // }

    // function reprojectGeoJSONIfNeeded(geojson) {
    //   const crsName = geojson?.crs?.properties?.name || "";
    //   if (!crsName.includes("2056")) return geojson;

    //   return {
    //     ...geojson,
    //     features: (geojson.features || []).map((feature) => ({
    //       ...feature,
    //       geometry: feature.geometry
    //         ? {
    //             ...feature.geometry,
    //             coordinates: reprojectCoordinateArray(feature.geometry.coordinates),
    //           }
    //         : feature.geometry,
    //     })),
    //   };
    // }

    function updateOverlayLayers() {}

    // function updateOverlayLayers(year) {
    //   Object.entries(overlayLayers).forEach(([label, layer]) => {
    //     if (label === "Limits") {
    //       // Handle GeoJSON limits layer
    //       layer.clearLayers();
    //       const url = limitsLayerUrls[year];
    //       if (url) {
    //         fetch(url)
    //           .then((res) => res.json())
    //           .then((data) => {
    //             const projectedData = reprojectGeoJSONIfNeeded(data);
    //             L.geoJSON(projectedData, {
    //               pane: "limitsPane",
    //               style: {
    //                 color: "#000000",
    //                 weight: 4,
    //                 opacity: 0.8,
    //               },
    //             }).addTo(layer);
    //           })
    //           .catch((err) => console.error(`Failed to load limits for ${year}:`, err));
    //       }
    //     } else {
    //       // Handle tile layer overlays
    //       const nextUrl = overlayLayerTemplates[label]?.[year] ?? transparentTileUrl;
    //       if (layer.setUrl) {
    //         layer.setUrl(nextUrl);
    //       }
    //     }
    //   });
    // }

    const activeTransportLayers = L.layerGroup().addTo(map);

    async function loadLayer(definition) {
      const response = await fetch(definition.url);

      if (!response.ok) {
        throw new Error(`Unable to load ${definition.url} (${response.status})`);
      }

      const data = await response.json();
      return L.geoJSON(data, {
        pane: "transportPane",
        style: {
          color: definition.color,
          weight: definition.weight,
          opacity: definition.opacity,
        },
      });
    }

    const transportLayersByYear = {};

    await Promise.all(
      yearSteps.map(async (year) => {
        const definitions = transportDefinitions[year] ?? [];
        transportLayersByYear[year] = await Promise.all(definitions.map(loadLayer));
      })
    );

    function showYear(year) {
      dateText.textContent = String(year);
      updateOverlayLayers(year);
      activeTransportLayers.clearLayers();

      const layers = transportLayersByYear[year] ?? [];
      layers.forEach((layer) => layer.addTo(activeTransportLayers));
    }

    slider.addEventListener("input", () => {
      const year = yearSteps[Number(slider.value)] ?? yearSteps[0];
      showYear(year);
    });

    function updateBackToTop() {
      const currentScrollY = window.scrollY || document.documentElement.scrollTop;
      backToTop.classList.toggle("hidden", currentScrollY < 200);
    }

    window.addEventListener("scroll", updateBackToTop, { passive: true });
    backToTop.addEventListener("click", (event) => {
      event.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    showYear(yearSteps[Number(slider.value)] ?? yearSteps[0]);
    updateBackToTop();
  })().catch((error) => {
    console.error(error);
  });
</script>

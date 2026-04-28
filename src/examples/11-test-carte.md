---
title: Test Carte 1983
toc: false
---

---

# 1907
```js
{
  const div = display(document.createElement("div"));
  div.style = "height: 600px; margin: 1em 0; border: 1px solid #ccc;";

  const mapBounds = [
    [46.48743, 6.51906], // SW
    [46.59011, 6.74191]  // NE
  ];

  // Center the map on Lausanne
  const map = L.map(div, {
    minZoom: 12,
    maxZoom: 16,
    maxBounds: mapBounds,
    maxBoundsViscosity: 1.0
  }).setView([46.45, 6.62], 13);

  // Keep transport layers in a dedicated pane above all raster tiles.
  map.createPane("transportPane");
  map.getPane("transportPane").style.zIndex = 650;

  // 1. Base Layer (OpenStreetMap)
  L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png", {
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);

  // 2. Historical map tiles (toggleable overlay)
  // In Observable Framework, static files are served from the /_file prefix.
  const historicalTiles = L.tileLayer("/_file/data/tiles_1983_v4/{z}/{x}/{y}.png", {
    opacity: 0.7,
    attribution: "Archives de Lausanne",
    minZoom: 12,
    maxZoom: 16 
  }).addTo(map);

  const transportLayers = L.layerGroup().addTo(map);

  // 1. Conversion approximative mm -> px
  const widthRail = 3.2; // ~0.86mm
  const widthRoute = 2.5; // ~0.66mm

  // // 1. On charge d'abord TOUTES les données en parallèle (plus rapide)
  const [tram1907, funiculaire1907, ferroviaire1907] = await Promise.all([
    FileAttachment("../data/trans_1907/1907_tram.geojson").json(),
    FileAttachment("../data/trans_1907/1907_funiculaire.geojson").json(),
    FileAttachment("../data/trans_1907/1907_train.geojson").json()
  ]);

  // const [rout1973] = await Promise.all([
  //   FileAttachment("../data/1973.geojson").json()
  // ]);
  // 2. Couche Tram
  L.geoJSON(tram1907, {
  pane: "transportPane",
  style: {
    color: "#b2df8a",
    weight: widthRoute,
    opacity: 0.9
  }
  }).addTo(transportLayers);

  // 3. Couche Ferroviaire (Train/Métro)
  L.geoJSON(ferroviaire1907, {
  pane: "transportPane",
  style: {
    color: "#e31a1c",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);

  // 4. Couche Funiculaire
  L.geoJSON(funiculaire1907, {
  pane: "transportPane",
  style: {
    color: "#fb9a99",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);


  L.control.layers({}, {
    "Historical Map (1983)": historicalTiles,
    "Transport Layers": transportLayers
  }, { collapsed: false }).addTo(map);

  invalidation.then(() => map.remove());
}
```

---

# 1925
```js
{
  const div = display(document.createElement("div"));
  div.style = "height: 600px; margin: 1em 0; border: 1px solid #ccc;";

  const mapBounds = [
    [46.48743, 6.51906], // SW
    [46.59011, 6.74191]  // NE
  ];

  // Center the map on Lausanne
  const map = L.map(div, {
    minZoom: 12,
    maxZoom: 16,
    maxBounds: mapBounds,
    maxBoundsViscosity: 1.0
  }).setView([46.45, 6.62], 13);

  // Keep transport layers in a dedicated pane above all raster tiles.
  map.createPane("transportPane");
  map.getPane("transportPane").style.zIndex = 650;

  // 1. Base Layer (OpenStreetMap)
  L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png", {
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);

  // 2. Historical map tiles (toggleable overlay)
  // In Observable Framework, static files are served from the /_file prefix.
  const historicalTiles = L.tileLayer("/_file/data/tiles_1983_v4/{z}/{x}/{y}.png", {
    opacity: 0.7,
    attribution: "Archives de Lausanne",
    minZoom: 12,
    maxZoom: 16 
  }).addTo(map);

  const transportLayers = L.layerGroup().addTo(map);

  // 1. Conversion approximative mm -> px
  const widthRail = 3.2; // ~0.86mm
  const widthRoute = 2.5; // ~0.66mm

  // // 1. On charge d'abord TOUTES les données en parallèle (plus rapide)
  const [rout1925, tram1925, funiculaire1925, ferroviaire1925] = await Promise.all([
    FileAttachment("../data/trans_1925/1925_bus.geojson").json(),
    FileAttachment("../data/trans_1925/1925_tram.geojson").json(),
    FileAttachment("../data/trans_1925/1925_funiculaire.geojson").json(),
    FileAttachment("../data/trans_1925/1925_train.geojson").json()
  ]);

  // const [rout1973] = await Promise.all([
  //   FileAttachment("../data/1973.geojson").json()
  // ]);

  // 1. Couche Bus
  L.geoJSON(rout1925, {
  pane: "transportPane",
  style: {
    color: "#1f78b4",
    weight: widthRoute,
    opacity: 0.9
  }
  }).addTo(transportLayers);

  // 2. Couche Tram
  L.geoJSON(tram1925, {
  pane: "transportPane",
  style: {
    color: "#b2df8a",
    weight: widthRoute,
    opacity: 0.9
  }
  }).addTo(transportLayers);

  // 3. Couche Ferroviaire (Train/Métro)
  L.geoJSON(ferroviaire1925, {
  pane: "transportPane",
  style: {
    color: "#e31a1c",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);

  // 4. Couche Funiculaire
  L.geoJSON(funiculaire1925, {
  pane: "transportPane",
  style: {
    color: "#fb9a99",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);


  L.control.layers({}, {
    "Historical Map (1983)": historicalTiles,
    "Transport Layers": transportLayers
  }, { collapsed: false }).addTo(map);

  invalidation.then(() => map.remove());
}
```

---

# 1937
```js
{
  const div = display(document.createElement("div"));
  div.style = "height: 600px; margin: 1em 0; border: 1px solid #ccc;";

  const mapBounds = [
    [46.48743, 6.51906], // SW
    [46.59011, 6.74191]  // NE
  ];

  // Center the map on Lausanne
  const map = L.map(div, {
    minZoom: 12,
    maxZoom: 16,
    maxBounds: mapBounds,
    maxBoundsViscosity: 1.0
  }).setView([46.45, 6.62], 13);

  // Keep transport layers in a dedicated pane above all raster tiles.
  map.createPane("transportPane");
  map.getPane("transportPane").style.zIndex = 650;

  // 1. Base Layer (OpenStreetMap)
  L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png", {
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);

  // 2. Historical map tiles (toggleable overlay)
  // In Observable Framework, static files are served from the /_file prefix.
  const historicalTiles = L.tileLayer("/_file/data/tiles_1983_v4/{z}/{x}/{y}.png", {
    opacity: 0.7,
    attribution: "Archives de Lausanne",
    minZoom: 12,
    maxZoom: 16 
  }).addTo(map);

  const transportLayers = L.layerGroup().addTo(map);

  // 1. Conversion approximative mm -> px
  const widthRail = 3.2; // ~0.86mm
  const widthRoute = 2.5; // ~0.66mm

  // // 1. On charge d'abord TOUTES les données en parallèle (plus rapide)
  const [tram1937, funiculaire1937, ferroviaire1937] = await Promise.all([
    FileAttachment("../data/trans_1937/1937_tram.geojson").json(),
    FileAttachment("../data/trans_1937/1937_funiculaire.geojson").json(),
    FileAttachment("../data/trans_1937/1937_train.geojson").json()
  ]);

  // const [rout1973] = await Promise.all([
  //   FileAttachment("../data/1973.geojson").json()
  // ]);
  // 2. Couche Tram
  L.geoJSON(tram1937, {
  pane: "transportPane",
  style: {
    color: "#b2df8a",
    weight: widthRoute,
    opacity: 0.9
  }
  }).addTo(transportLayers);

  // 3. Couche Ferroviaire (Train/Métro)
  L.geoJSON(ferroviaire1937, {
  pane: "transportPane",
  style: {
    color: "#e31a1c",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);

  // 4. Couche Funiculaire
  L.geoJSON(funiculaire1937, {
  pane: "transportPane",
  style: {
    color: "#fb9a99",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);


  L.control.layers({}, {
    "Historical Map (1983)": historicalTiles,
    "Transport Layers": transportLayers
  }, { collapsed: false }).addTo(map);

  invalidation.then(() => map.remove());
}
```


---

# 1973
```js
{
  const div = display(document.createElement("div"));
  div.style = "height: 600px; margin: 1em 0; border: 1px solid #ccc;";

  const mapBounds = [
    [46.48743, 6.51906], // SW
    [46.59011, 6.74191]  // NE
  ];

  // Center the map on Lausanne
  const map = L.map(div, {
    minZoom: 12,
    maxZoom: 16,
    maxBounds: mapBounds,
    maxBoundsViscosity: 1.0
  }).setView([46.45, 6.62], 13);

  // Keep transport layers in a dedicated pane above all raster tiles.
  map.createPane("transportPane");
  map.getPane("transportPane").style.zIndex = 650;

  // 1. Base Layer (OpenStreetMap)
  L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png", {
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);

  // 2. Historical map tiles (toggleable overlay)
  // In Observable Framework, static files are served from the /_file prefix.
  const historicalTiles = L.tileLayer("/_file/data/tiles_1983_v4/{z}/{x}/{y}.png", {
    opacity: 0.7,
    attribution: "Archives de Lausanne",
    minZoom: 12,
    maxZoom: 16 
  }).addTo(map);

  const transportLayers = L.layerGroup().addTo(map);

  // 1. Conversion approximative mm -> px
  const widthRail = 3.2; // ~0.86mm
  const widthRoute = 2.5; // ~0.66mm

  // // 1. On charge d'abord TOUTES les données en parallèle (plus rapide)
  const [rout1973, funiculaire1973, ferroviaire1973] = await Promise.all([
    FileAttachment("../data/trans_1973/1973_busv3.geojson").json(),
    FileAttachment("../data/trans_1973/1973_funi.geojson").json(),
    FileAttachment("../data/trans_1973/1973_ferv2.geojson").json()
  ]);

  // const [rout1973] = await Promise.all([
  //   FileAttachment("../data/1973.geojson").json()
  // ]);
  // 2. Couche Routière (Lignes de bus/troley)
  L.geoJSON(rout1973, {
  pane: "transportPane",
  style: {
    color: "#1f78b4",
    weight: widthRoute,
    opacity: 0.9
  }
  }).addTo(transportLayers);

  // 3. Couche Ferroviaire (Train/Métro)
  L.geoJSON(ferroviaire1973, {
  pane: "transportPane",
  style: {
    color: "#e31a1c",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);

  // 4. Couche Funiculaire
  L.geoJSON(funiculaire1973, {
  pane: "transportPane",
  style: {
    color: "#fb9a99",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);


  L.control.layers({}, {
    "Historical Map (1983)": historicalTiles,
    "Transport Layers": transportLayers
  }, { collapsed: false }).addTo(map);

  invalidation.then(() => map.remove());
}
```

---

# 1983

```js
{
  const div = display(document.createElement("div"));
  div.style = "height: 600px; margin: 1em 0; border: 1px solid #ccc;";

  const mapBounds = [
    [46.48743, 6.51906], // SW
    [46.59011, 6.74191]  // NE
  ];

  // Center the map on Lausanne
  const map = L.map(div, {
    minZoom: 12,
    maxZoom: 16,
    maxBounds: mapBounds,
    maxBoundsViscosity: 1.0
  }).setView([46.45, 6.62], 13);

  // Keep transport layers in a dedicated pane above all raster tiles.
  map.createPane("transportPane");
  map.getPane("transportPane").style.zIndex = 650;

  // 1. Base Layer (OpenStreetMap)
  L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png", {
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);

  // 2. Historical map tiles (toggleable overlay)
  // In Observable Framework, static files are served from the /_file prefix.
  const historicalTiles = L.tileLayer("/_file/data/tiles_1983_v4/{z}/{x}/{y}.png", {
    opacity: 0.7,
    attribution: "Archives de Lausanne",
    minZoom: 12,
    maxZoom: 16 
  }).addTo(map);

  const transportLayers = L.layerGroup().addTo(map);

  // 1. Conversion approximative mm -> px
  const widthRail = 3.2; // ~0.86mm
  const widthRoute = 2.5; // ~0.66mm

  // 1. On charge d'abord TOUTES les données en parallèle (plus rapide)
  const [rout1983, funiculaire1983, ferroviaire1983] = await Promise.all([
    FileAttachment("../data/trans_1983/rout_ligne_v2.geojson").json(),
    FileAttachment("../data/trans_1983/funiculaire.geojson").json(),
    FileAttachment("../data/trans_1983/ferroviaire_v2.geojson").json()
  ]);

  // 2. Couche Routière (Lignes de bus/troley)
  L.geoJSON(rout1983, {
  pane: "transportPane",
  style: {
    color: "#1f78b4",
    weight: widthRoute,
    opacity: 0.9
  }
  }).addTo(transportLayers);

  // 3. Couche Ferroviaire (Train/Métro)
  L.geoJSON(ferroviaire1983, {
  pane: "transportPane",
  style: {
    color: "#e31a1c",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);

  // 4. Couche Funiculaire
  L.geoJSON(funiculaire1983, {
  pane: "transportPane",
  style: {
    color: "#fb9a99",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);

  // L.geoJSON(funiculaire1983, {
  //   pane: "transportPane",
  //   style: {
  //     color: "#8e44ad",
  //     weight: 3,
  //     opacity: 0.9
  //   }
  // }).addTo(transportLayers).bringToFront();

  // L.geoJSON(ferroviaire1983, {
  //   pane: "transportPane",
  //   style: {
  //     color: "#2980b9",
  //     weight: 3,
  //     opacity: 0.9
  //   }
  // }).addTo(transportLayers).bringToFront();

  L.control.layers({}, {
    "Historical Map (1983)": historicalTiles,
    "Transport Layers": transportLayers
  }, { collapsed: false }).addTo(map);

  invalidation.then(() => map.remove());
}
```

---
# 2000

```js
{
  const div = display(document.createElement("div"));
  div.style = "height: 600px; margin: 1em 0; border: 1px solid #ccc;";

  const mapBounds = [
    [46.48743, 6.51906], // SW
    [46.59011, 6.74191]  // NE
  ];

  // Center the map on Lausanne
  const map = L.map(div, {
    minZoom: 12,
    maxZoom: 16,
    maxBounds: mapBounds,
    maxBoundsViscosity: 1.0
  }).setView([46.45, 6.62], 13);

  // Keep transport layers in a dedicated pane above all raster tiles.
  map.createPane("transportPane");
  map.getPane("transportPane").style.zIndex = 650;

  // 1. Base Layer (OpenStreetMap)
  L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png", {
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);

  // 2. Historical map tiles (toggleable overlay)
  // In Observable Framework, static files are served from the /_file prefix.
  const historicalTiles = L.tileLayer("/_file/data/tiles_1983_v4/{z}/{x}/{y}.png", {
    opacity: 0.7,
    attribution: "Archives de Lausanne",
    minZoom: 12,
    maxZoom: 16 
  }).addTo(map);

  const transportLayers = L.layerGroup().addTo(map);

  // 1. Conversion approximative mm -> px
  const widthRail = 3.2; // ~0.86mm
  const widthRoute = 2.5; // ~0.66mm

  // 1. On charge d'abord TOUTES les données en parallèle (plus rapide)
  const [rout1983, funiculaire1983, ferroviaire1983] = await Promise.all([
    FileAttachment("../data/trans_2000/ROUTE_ligne_2000.geojson").json(),
    FileAttachment("../data/trans_2000/FUNI_ligne_2000.geojson").json(),
    FileAttachment("../data/trans_2000/FER_ligne_2000.geojson").json()
  ]);

  // 2. Couche Routière (Lignes de bus/troley)
  L.geoJSON(rout1983, {
  pane: "transportPane",
  style: {
    color: "#1f78b4",
    weight: widthRoute,
    opacity: 0.9
  }
  }).addTo(transportLayers);

  // 3. Couche Ferroviaire (Train/Métro)
  L.geoJSON(ferroviaire1983, {
  pane: "transportPane",
  style: {
    color: "#e31a1c",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);

  // 4. Couche Funiculaire
  L.geoJSON(funiculaire1983, {
  pane: "transportPane",
  style: {
    color: "#fb9a99",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);

  // L.geoJSON(funiculaire1983, {
  //   pane: "transportPane",
  //   style: {
  //     color: "#8e44ad",
  //     weight: 3,
  //     opacity: 0.9
  //   }
  // }).addTo(transportLayers).bringToFront();

  // L.geoJSON(ferroviaire1983, {
  //   pane: "transportPane",
  //   style: {
  //     color: "#2980b9",
  //     weight: 3,
  //     opacity: 0.9
  //   }
  // }).addTo(transportLayers).bringToFront();

  L.control.layers({}, {
    "Historical Map (1983)": historicalTiles,
    "Transport Layers": transportLayers
  }, { collapsed: false }).addTo(map);

  invalidation.then(() => map.remove());
}
```

---

# 2025

```js
{
  const div = display(document.createElement("div"));
  div.style = "height: 600px; margin: 1em 0; border: 1px solid #ccc;";

  const mapBounds = [
    [46.48743, 6.51906], // SW
    [46.59011, 6.74191]  // NE
  ];

  // Center the map on Lausanne
  const map = L.map(div, {
    minZoom: 12,
    maxZoom: 16,
    maxBounds: mapBounds,
    maxBoundsViscosity: 1.0
  }).setView([46.45, 6.62], 13);

  // Keep transport layers in a dedicated pane above all raster tiles.
  map.createPane("transportPane");
  map.getPane("transportPane").style.zIndex = 650;

  // 1. Base Layer (OpenStreetMap)
  L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png", {
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);

  // 2. Historical map tiles (toggleable overlay)
  // In Observable Framework, static files are served from the /_file prefix.
  const historicalTiles = L.tileLayer("/_file/data/tiles_1983_v4/{z}/{x}/{y}.png", {
    opacity: 0.7,
    attribution: "Archives de Lausanne",
    minZoom: 12,
    maxZoom: 16 
  }).addTo(map);

  const transportLayers = L.layerGroup().addTo(map);

  // 1. Conversion approximative mm -> px
  const widthRail = 3.2; // ~0.86mm
  const widthRoute = 2.5; // ~0.66mm

  // 1. On charge d'abord TOUTES les données en parallèle (plus rapide)
  const [rout2025, ferroviaire2025] = await Promise.all([
    FileAttachment("../data/trans_2025/ROUTE_ligne_2025.geojson").json(),
    FileAttachment("../data/trans_2025/FER_ligne_2025.geojson").json()
  ]);

  // 2. Couche Routière (Lignes de bus/troley)
  L.geoJSON(rout2025, {
  pane: "transportPane",
  style: {
    color: "#1f78b4",
    weight: widthRoute,
    opacity: 0.9
  }
  }).addTo(transportLayers);

  // 3. Couche Ferroviaire (Train/Métro)
  L.geoJSON(ferroviaire2025, {
  pane: "transportPane",
  style: {
    color: "#e31a1c",
    weight: widthRail,
    opacity: 1
  }
  }).addTo(transportLayers);


  L.control.layers({}, {
    "Historical Map (1983)": historicalTiles,
    "Transport Layers": transportLayers
  }, { collapsed: false }).addTo(map);

  invalidation.then(() => map.remove());
}
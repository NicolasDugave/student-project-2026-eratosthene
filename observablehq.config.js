// See https://observablehq.com/framework/config

export default {
  title: "Lausanne Time Machine",

  pages: [
    {
      name: "Navigation",
      pages: [
        { name: "Accueil", path: "/index" },
        { name: "Analyses historiques", path: "/analyse" },
        { name: "Sources", path: "/sources" }
      ]
    }
  ],

  head: `
    <link rel="icon" href="observable.png" type="image/png" sizes="32x32">
  `,

  root: "src",

  theme: "light",

  footer:
    "2025–2026 · Lausanne Time Machine · EPFL",

  sidebar: {
    collapsible: false
  },

  pager: false,

  toc: false
};
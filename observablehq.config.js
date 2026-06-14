// See https://observablehq.com/framework/config for documentation.
export default {
  // The project’s title; used in the sidebar and webpage titles.
  title: "Nico Purnomo",

  // The pages and sections in the sidebar. If you don’t specify this option,
  // all pages will be listed in alphabetical order. Listing pages explicitly
  // lets you organize them into sections and have unlisted pages.
  pages: [
    {name: "About", path: "/about"},
    {
      name: "Work",
      pages: [
        {name: "World Cup Pub — 0→1 in 48hrs", path: "/09-World-Cup-Pub"},
        {name: "World Cup Pub, Part 2 — Steering the Agent", path: "/10-World-Cup-Pub-2"},
        {name: "Industry Financials", path: "/03-Finance-dashb"},
        {name: "Remember Covid?", path: "/05-covid"},
        {name: "Earthquakes and Extreme Values", path: "/06-Earthquake_PoT"},
        {name: "SQL Away!", path: "/07-Customer-dashb"},
        {name: "Heathrow Forecast", path: "/08-Heathrow-forecast"},
        {name: "About Up Banking", path: "/01-Up-article"},
        {name: "Simile, Here, and Everywhere", path: "/02-Simile-article"},
        {name: "Data Reduction", path: "/04-Data-Reduction-article"},
      ]
    },
  ],

  // Some additional configuration options and their defaults:
  // theme: "default", // try "light", "dark", "slate", etc.
  // header: "", // what to show in the header (HTML)
  // footer: "Built with Observable.", // what to show in the footer (HTML)
  // toc: true, // whether to show the table of contents
  // pager: true, // whether to show previous & next links in the footer
  // root: "docs", // path to the source root for preview
  // output: "dist", // path to the output root for build
  search: true, // activate search
};

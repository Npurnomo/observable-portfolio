---
toc: false
---

<style>
.hero {
  margin: 4rem 0 3rem;
  font-family: var(--sans-serif);
}
.hero h1 {
  font-size: clamp(36px, 6vw, 72px);
  font-weight: 700;
  line-height: 1.1;
  margin: 0 0 0.5rem;
  color: var(--theme-foreground-focus);
}
.hero h2 {
  font-size: 20px;
  font-weight: 400;
  color: var(--theme-foreground-muted);
  margin: 0 0 1rem;
}
.hero p {
  font-size: 16px;
  max-width: 520px;
  color: var(--theme-foreground);
  margin: 0 0 1rem;
  line-height: 1.6;
}
.hero .terminal-link {
  font-family: var(--monospace);
  font-size: 13px;
  color: var(--theme-foreground-muted);
  text-decoration: none;
}
.hero .terminal-link:hover {
  color: var(--theme-foreground-focus);
}
</style>

<div class="hero">
  <h1>Nico Purnomo</h1>
  <h2>Product manager. Data, ML, and the occasional rabbit hole.</h2>
  <p>I build data, ML, and AI products professionally, and share the analytical side here — interactive projects, articles, and ideas I find interesting.</p>
  <a href="https://terminal-website-npurnomo.vercel.app/" class="terminal-link">↗ terminal-website-npurnomo.vercel.app</a>
</div>

<div class="grid grid-cols-2" style="grid-auto-rows: 400px;">
  <div class="card">${
    resize((width) => Plot.plot({
      title: "NVIDIA (NVDA) Stock Price",
      subtitle: "Monthly close, split-adjusted, 2020–2024. The AI era in one chart.",
      width,
      height: 320,
      y: {grid: true, label: "Price (USD)"},
      x: {label: "Date"},
      marks: [
        Plot.ruleY([0]),
        Plot.lineY(nvda, {x: "Date", y: "Close", tip: true, stroke: "#89AB6C"})
      ]
    }))
  }</div>
  <div class="card">${
    resize((width) => Plot.plot({
      title: "Global Earthquakes 2001–2023",
      subtitle: "782 significant events. Ring of Fire clearly visible.",
      width,
      height: 350,
      projection: "equirectangular",
      r: {range: [1, 6]},
      marks: [
        Plot.geo(land, {fill: "#000", fillOpacity: 0.4}),
        Plot.dot(earthquake, {
          x: "longitude",
          y: "latitude",
          r: "sig",
          fill: "#dab56a",
          fillOpacity: 0.6,
          tip: false
        })
      ]
    }))
  }</div>
</div>

```js
import * as topojson from "npm:topojson-client";
const nvda = await FileAttachment("nvda.csv").csv({typed: true});
const earthquake = await FileAttachment("data/earthquake_1995-2023.csv").csv({typed: true});
const land50m = await FileAttachment("data/land-50m.json").json();
const land = topojson.feature(land50m, land50m.objects.land);
```

---

<div class="grid grid-cols-4">
  <div class="card">
    <strong>Get in touch</strong><br>
    <a href="mailto:purnomonico@gmail.com">purnomonico@gmail.com</a><br>
    <a href="https://www.linkedin.com/in/nico-purnomo/">LinkedIn</a>
  </div>
  <div class="card">
    <strong>Terminal site</strong><br>
    An interactive CLI version of this portfolio.<br>
    <a href="https://terminal-website-npurnomo.vercel.app/">Open terminal ↗</a>
  </div>
</div>

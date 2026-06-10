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

<style>
.section-label {
  font-family: var(--monospace);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--theme-foreground-muted);
  margin: 2rem 0 0.75rem;
}
.work-card {
  display: block;
  text-decoration: none;
  color: inherit;
  padding: 1rem;
  border: 1px solid var(--theme-foreground-faintest);
  border-radius: 8px;
  transition: border-color 200ms ease;
  height: 100%;
}
.work-card:hover { border-color: #dab56a; }
.work-card h3 {
  font-size: 15px;
  font-weight: 600;
  margin: 0 0 0.35rem;
  color: var(--theme-foreground-focus);
}
.work-card p {
  font-size: 13px;
  color: var(--theme-foreground-muted);
  margin: 0 0 0.75rem;
  line-height: 1.5;
}
.tags { display: flex; flex-wrap: wrap; gap: 4px; }
.tag {
  font-family: var(--monospace);
  font-size: 10px;
  color: #89AB6C;
  background: var(--theme-background-alt);
  border: 1px solid var(--theme-foreground-faintest);
  border-radius: 3px;
  padding: 1px 6px;
}
.contact-row {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--theme-foreground-faintest);
  font-size: 14px;
  color: var(--theme-foreground-muted);
}
.contact-row a {
  color: var(--theme-foreground-muted);
  text-decoration: none;
  margin-right: 1.25rem;
}
.contact-row a:hover { color: #dab56a; }
</style>

<p class="section-label">Case Studies</p>
<div class="grid grid-cols-1">
  <a class="work-card" href="./09-World-Cup-Pub">
    <h3>World Cup Pub — 0→1 in 48 Hours</h3>
    <p>Mobile-first app that helps London football fans find and book a pub to watch the 2026 World Cup. Built in 48 hours. Full build story: spec, architecture, agent workflow, post-launch bugs.</p>
    <div class="tags"><span class="tag">product</span><span class="tag">Next.js</span><span class="tag">TypeScript</span><span class="tag">Google Maps</span></div>
  </a>
</div>

<p class="section-label">Projects</p>
<div class="grid grid-cols-3">
  <a class="work-card" href="./03-Finance-dashb">
    <h3>Industry Financials</h3>
    <p>Interactive dashboard comparing financial metrics across US industries. Built on Damodaran's public data — pick any two metrics and explore.</p>
    <div class="tags"><span class="tag">finance</span><span class="tag">dashboard</span><span class="tag">Observable Plot</span></div>
  </a>
  <a class="work-card" href="./05-covid">
    <h3>Remember Covid?</h3>
    <p>Time series of excess deaths by country using The Economist's model. Confidence bands show estimation uncertainty across 2020–2024.</p>
    <div class="tags"><span class="tag">time-series</span><span class="tag">public health</span><span class="tag">Observable Plot</span></div>
  </a>
  <a class="work-card" href="./06-Earthquake_PoT">
    <h3>Earthquakes & Extreme Values</h3>
    <p>Global seismic data mapped and modelled with Generalised Pareto Distribution. Estimates the probability of extreme magnitude events.</p>
    <div class="tags"><span class="tag">statistics</span><span class="tag">mapping</span><span class="tag">R</span></div>
  </a>
  <a class="work-card" href="./07-Customer-dashb">
    <h3>SQL Away!</h3>
    <p>Write SQL queries live in the browser against a customer orders dataset. Powered by DuckDB-WASM — no server, runs entirely client-side.</p>
    <div class="tags"><span class="tag">SQL</span><span class="tag">DuckDB</span><span class="tag">interactive</span></div>
  </a>
  <a class="work-card" href="./08-Heathrow-forecast">
    <h3>Heathrow Forecast</h3>
    <p>ARIMA time series model forecasting passenger traffic at Heathrow. Accounts for Covid impact via dummy variable — with and without comparison.</p>
    <div class="tags"><span class="tag">forecasting</span><span class="tag">ARIMA</span><span class="tag">R</span></div>
  </a>
</div>

<p class="section-label">Articles</p>
<div class="grid grid-cols-2">
  <a class="work-card" href="./01-Up-article">
    <h3>Up Banking & Neobanks (2021)</h3>
    <p>How digital-only banks navigated the pandemic, what Xinja's collapse meant for the industry, and why Up's model was different.</p>
    <div class="tags"><span class="tag">fintech</span><span class="tag">writing</span></div>
  </a>
  <a class="work-card" href="./02-Simile-article">
    <h3>Simile, Here & Everywhere (2023)</h3>
    <p>On similarity as a concept — from cosine distance to clustering to recommendation systems. Why measuring likeness is harder than it looks.</p>
    <div class="tags"><span class="tag">statistics</span><span class="tag">ML</span><span class="tag">writing</span></div>
  </a>
  <a class="work-card" href="./04-Data-Reduction-article">
    <h3>Data Reduction through Dynamic Range (2023)</h3>
    <p>Dynamic range, audio compression, and SVD — a unified lens on what it means to reduce complexity while preserving meaning.</p>
    <div class="tags"><span class="tag">data</span><span class="tag">SVD</span><span class="tag">writing</span></div>
  </a>
</div>

<div class="contact-row">
  <a href="mailto:purnomonico@gmail.com">purnomonico@gmail.com</a>
  <a href="https://www.linkedin.com/in/nico-purnomo/">LinkedIn</a>
  <a href="https://github.com/Npurnomo">GitHub</a>
  <a href="https://purnomonico.medium.com/">Medium</a>
</div>

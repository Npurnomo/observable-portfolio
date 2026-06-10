---
toc: false
---

<style>
.hero {
  margin: 4rem 0 2.5rem;
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
.hero .terminal-link:hover { color: var(--theme-foreground-focus); }

/* Featured card */
.featured {
  border: 1px solid #dab56a;
  border-radius: 8px;
  padding: 1.75rem;
  margin-bottom: 0.5rem;
  background: var(--theme-background-alt);
}
.featured-meta {
  font-family: var(--monospace);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #dab56a;
  margin: 0 0 0.75rem;
}
.featured h2 {
  font-size: clamp(20px, 3vw, 28px);
  font-weight: 700;
  margin: 0 0 0.75rem;
  color: var(--theme-foreground-focus);
}
.featured > p {
  font-size: 15px;
  color: var(--theme-foreground);
  max-width: 640px;
  line-height: 1.65;
  margin: 0 0 1.25rem;
}
.featured-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 0 1.5rem;
  font-family: var(--monospace);
  font-size: 12px;
  color: var(--theme-foreground-muted);
  margin-bottom: 1.5rem;
}
.featured-links {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}
.featured-links .btn-live {
  background: #dab56a;
  color: #141923;
  font-weight: 600;
  font-size: 13px;
  padding: 7px 16px;
  border-radius: 4px;
  text-decoration: none;
  transition: background 150ms ease;
}
.featured-links .btn-live:hover { background: #c9a45a; }
.featured-links .btn-story {
  font-size: 13px;
  color: var(--theme-foreground-muted);
  text-decoration: none;
  transition: color 150ms ease;
}
.featured-links .btn-story:hover { color: var(--theme-foreground-focus); }

/* Work cards */
.section-label {
  font-family: var(--monospace);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--theme-foreground-muted);
  margin: 2.25rem 0 0.75rem;
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

/* Contact */
.contact-row {
  margin-top: 2.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--theme-foreground-faintest);
  font-size: 14px;
}
.contact-row a {
  color: var(--theme-foreground-muted);
  text-decoration: none;
  margin-right: 1.25rem;
}
.contact-row a:hover { color: #dab56a; }
</style>

<div class="hero">
  <h1>Nico Purnomo</h1>
  <h2>Product manager. Data, ML, and the occasional rabbit hole.</h2>
  <p>I build data, ML, and AI products professionally, and share the analytical side here — interactive projects, articles, and ideas I find interesting.</p>
  <a href="https://terminal-website-npurnomo.vercel.app/" class="terminal-link">↗ terminal-website-npurnomo.vercel.app</a>
</div>

<p class="section-label">Latest</p>
<div class="featured">
  <p class="featured-meta">Case Study · June 2026</p>
  <h2>World Cup Pub — 0→1 in 48 Hours</h2>
  <p>Mobile-first web app that helps London football fans find and book a pub for the 2026 World Cup. Built from idea to live in 48 hours: product spec, Jira backlog, React frontend, Google Maps integration, Vercel deploy. Post-mortem covers architecture decisions, two post-launch bugs, and what the agent workflow actually looked like.</p>
  <div class="featured-stats">
    <span>48 hrs idea → live</span>
    <span>Next.js · TypeScript</span>
    <span>Google Maps API</span>
    <span>0 TypeScript errors</span>
    <span>Live during the 2026 World Cup</span>
  </div>
  <div class="featured-links">
    <a href="https://world-cup-pub.vercel.app" class="btn-live" target="_blank">Live app ↗</a>
    <a href="./09-World-Cup-Pub" class="btn-story">Read the build story →</a>
  </div>
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

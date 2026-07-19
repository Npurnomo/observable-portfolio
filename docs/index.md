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

/* Featured */
.featured {
  border: 1px solid #dab56a;
  border-radius: 8px;
  padding: 1.75rem;
  margin-bottom: 2rem;
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

/* Section label */
.section-label {
  font-family: var(--monospace);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--theme-foreground-muted);
  margin: 0 0 0.75rem;
  display: block;
}

/* Work cards */
.work-card {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
  padding: 1rem;
  border: 1px solid var(--theme-foreground-faintest);
  border-radius: 8px;
  transition: border-color 200ms ease;
}
.work-card:hover { border-color: #dab56a; }
.work-card h3 {
  font-size: 14px;
  font-weight: 600;
  margin: 0 0 0.4rem;
  color: var(--theme-foreground-focus);
  line-height: 1.3;
}
.work-card p {
  font-size: 12px;
  color: var(--theme-foreground-muted);
  margin: 0 0 0.75rem;
  line-height: 1.5;
  flex: 1;
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

<span class="section-label">Latest</span>
<div class="featured">
  <p class="featured-meta">Case Study · July 2026</p>
  <h2>Quorum — Cost per Correct Decision</h2>
  <p>An eval-governed control plane for visual AI decisions, built deliberately on a weak detector to prove the system matters more than the model. Confidence routing across a cheap detector, a vision-language model, and a human queue — every decision priced and recorded. The eval harness caught the detector naming 3 of 514 objects correctly, watched a drift alarm fire on cue, and picked up a never-trained class zero-shot. Includes an animated explainer with a locally-synthesized voiceover.</p>
  <div class="featured-stats">
    <span>5 build phases</span>
    <span>£0.00 of a £10 cap spent</span>
    <span>271 tests</span>
    <span>87% decided in ~0.5s</span>
    <span>LangGraph · Qwen2.5-VL · CLIP</span>
  </div>
  <div class="featured-links">
    <a href="./11-Quorum" class="btn-live">Read the case study →</a>
  </div>
</div>

<span class="section-label">Work</span>
<div class="grid grid-cols-4">
  <a class="work-card" href="./09-World-Cup-Pub">
    <h3>World Cup Pub: 0→1 in 48 Hours</h3>
    <p>From idea to live app in 48 hours — spec, Jira backlog, React frontend, Maps integration, deploy. Post-mortem with the bugs left in.</p>
    <div class="tags"><span class="tag">product</span><span class="tag">Next.js</span><span class="tag">0→1</span></div>
  </a>
  <a class="work-card" href="./10-World-Cup-Pub-2">
    <h3>World Cup Pub, Part 2: Steering the Agent</h3>
    <p>The human side of a 48-hour AI-assisted build — what I caught, missed, and would do differently. Covers failure taxonomy, prompt discipline, and a repeatable eval checklist.</p>
    <div class="tags"><span class="tag">AI</span><span class="tag">product</span><span class="tag">writing</span></div>
  </a>
  <a class="work-card" href="./03-Finance-dashb">
    <h3>Industry Financials</h3>
    <p>Interactive dashboard comparing financial metrics across US industries. Pick any two metrics and explore the relationships.</p>
    <div class="tags"><span class="tag">finance</span><span class="tag">dashboard</span><span class="tag">Observable Plot</span></div>
  </a>
  <a class="work-card" href="./05-covid">
    <h3>Remember Covid?</h3>
    <p>Excess death estimates by country using The Economist's model. Confidence bands show estimation uncertainty across 2020–2024.</p>
    <div class="tags"><span class="tag">time-series</span><span class="tag">public health</span></div>
  </a>
  <a class="work-card" href="./06-Earthquake_PoT">
    <h3>Earthquakes & Extreme Values</h3>
    <p>Global seismic data mapped and modelled with Generalised Pareto Distribution. Estimates the probability of extreme magnitude events.</p>
    <div class="tags"><span class="tag">statistics</span><span class="tag">mapping</span><span class="tag">R</span></div>
  </a>
  <a class="work-card" href="./07-Customer-dashb">
    <h3>SQL Away!</h3>
    <p>Write SQL queries live in the browser against a customer orders dataset. Powered by DuckDB-WASM — no server required.</p>
    <div class="tags"><span class="tag">SQL</span><span class="tag">DuckDB</span><span class="tag">interactive</span></div>
  </a>
  <a class="work-card" href="./08-Heathrow-forecast">
    <h3>Heathrow Forecast</h3>
    <p>ARIMA model forecasting passenger traffic at Heathrow. Dummy variable accounts for Covid — with and without comparison.</p>
    <div class="tags"><span class="tag">forecasting</span><span class="tag">ARIMA</span><span class="tag">R</span></div>
  </a>
  <a class="work-card" href="./01-Up-article">
    <h3>Up Banking & Neobanks</h3>
    <p>How digital-only banks navigated the pandemic, what Xinja's collapse meant for the industry, and why Up's model was different.</p>
    <div class="tags"><span class="tag">fintech</span><span class="tag">writing</span></div>
  </a>
  <a class="work-card" href="./02-Simile-article">
    <h3>Simile, Here & Everywhere</h3>
    <p>On similarity as a concept — from cosine distance to clustering to recommendation systems. Why measuring likeness is harder than it looks.</p>
    <div class="tags"><span class="tag">statistics</span><span class="tag">ML</span><span class="tag">writing</span></div>
  </a>
  <a class="work-card" href="./04-Data-Reduction-article">
    <h3>Data Reduction through Dynamic Range</h3>
    <p>Audio compression, photography, and SVD — a unified lens on what it means to reduce complexity while preserving meaning.</p>
    <div class="tags"><span class="tag">data</span><span class="tag">SVD</span><span class="tag">writing</span></div>
  </a>
</div>

<div class="contact-row">
  <a href="mailto:purnomonico@gmail.com">purnomonico@gmail.com</a>
  <a href="https://www.linkedin.com/in/nico-purnomo/">LinkedIn</a>
  <a href="https://github.com/Npurnomo">GitHub</a>
  <a href="https://purnomonico.medium.com/">Medium</a>
</div>

---
toc: false
---

<style>

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--sans-serif);
  margin: 4rem 0 8rem;
  text-wrap: balance;
  text-align: center;
}

.hero h1 {
  margin: 2rem 0;
  max-width: none;
  font-size: 14vw;
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(30deg, var(--theme-foreground-focus), currentColor);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero h2 {
  margin: 0;
  max-width: 40em;
  font-size: 20px;
  font-style: initial;
  font-weight: 500;
  line-height: 1.5;
  color: var(--theme-foreground-muted);
}

@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}

</style>

<div class="hero">
  <h1>Hello!!! </h1>
  <h2>Welcome to Nico Purnomo's Observable site! We are just getting started 🚀. I will be sharing articles, dashboards, and hopefully digestible ideas here. Watch this space 👀 👀</h2>
</div>

### Sample quick dashboards

<div class="grid grid-cols-2" style="grid-auto-rows: 504px;">
  <div class="card">${
    resize((width) => Plot.plot({
      title: "Apple Stock Price 🍏📈 for fun",
      subtitle: "",
      width,
      y: {grid: true, label: "Price"},
      marks: [
        Plot.ruleY([0]),
        Plot.lineY(aapl, {x: "Date", y: "Close", tip: true})
      ]
    }))
  }</div>
  <div class="card">${
    resize((width) => Plot.plot({
      title: "How big are penguins, anyway? 🐧",
      width,
      grid: true,
      x: {label: "Body mass (g)"},
      y: {label: "Flipper length (mm)"},
      color: {legend: true},
      marks: [
        Plot.linearRegressionY(penguins, {x: "body_mass_g", y: "flipper_length_mm", stroke: "species"}),
        Plot.dot(penguins, {x: "body_mass_g", y: "flipper_length_mm", stroke: "species", tip: true})
      ]
    }))
  }</div>
</div>

```js
const aapl = FileAttachment("aapl.csv").csv({typed: true});
const penguins = FileAttachment("penguins.csv").csv({typed: true});
```

---

### The sidebar on the left side is for navigation. Click on anything that interests you!



<div class="grid grid-cols-4">

  <div class="card">
    Contact me <a href="https://www.linkedin.com/in/nico-purnomo/">here</a> on <code>Linkedin</code> or email me on <a href="mailto:purnomonico@gmail.com">purnomonico@gmail.com</a>
  </div>
  <div class="card">
    Check out my Terminal styled website  <a href="https://terminal-website-npurnomo.vercel.app/">here</a>.
  </div>
</div>

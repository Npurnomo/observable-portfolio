---
title: Remember Covid?
toc: false
---

# Remember COVID-19?

Showing excess death estimates for **${country}**

I graduated my undergrad in 2020, and the COVID-19 pandemic was a significant part of my final semester. I still remember the fear and uncertainty that gripped the world as the virus spread rapidly across countries. The pandemic changed the way we live, work, and interact with each other. Venturing about the job market mid 2020 was difficult, but I was lucky to have found a role through my personal data projects then.

This page gives a brief look at how COVID-19 affected different countries through the lens of **excess deaths** — the difference between observed deaths and what would have been expected without the pandemic. Data is sourced from [The Economist's global excess deaths model](https://github.com/TheEconomist/covid-19-the-economist-global-excess-deaths-model).

```js
const allData = await FileAttachment("data/covid-excess-deaths.csv").csv({ typed: true });
const countries = [...new Set(allData.map(d => d.location))].sort();
```

```js
const country = view(Inputs.select(countries, {
  value: "Albania",
  label: "Country"
}));
```

```js
const country_data = allData
  .filter(d => d.location === country)
  .map(d => ({
    ...d,
    date: new Date(d.date),
    estimate: +d.estimate,
    estimate_top_95: +d.estimate_top_95,
    estimate_top_50: +d.estimate_top_50,
    estimate_bot_50: +d.estimate_bot_50,
    estimate_bot_95: +d.estimate_bot_95,
    official_covid_deaths: d.official_covid_deaths === "NA" ? null : +d.official_covid_deaths
  }));
```

```js
Plot.plot({
  y: {
    grid: true,
    label: "Estimated daily excess deaths"
  },
  x: { label: "Date" },
  width,
  marginLeft: 60,
  marks: [
    Plot.areaY(country_data, {
      x: "date",
      y1: "estimate_bot_95",
      y2: "estimate_top_95",
      fill: "#89AB6C",
      fillOpacity: 0.15
    }),
    Plot.areaY(country_data, {
      x: "date",
      y1: "estimate_bot_50",
      y2: "estimate_top_50",
      fill: "#89AB6C",
      fillOpacity: 0.25
    }),
    Plot.lineY(country_data, {
      x: "date",
      y: "estimate",
      stroke: "#89AB6C",
      tip: true
    }),
    Plot.ruleY([0], { stroke: "var(--theme-foreground-faintest)" })
  ]
})
```

```js
Inputs.table(country_data, {
  columns: ["date", "estimate", "official_covid_deaths"],
  header: {
    date: "Date",
    estimate: "Est. daily excess deaths",
    official_covid_deaths: "Official COVID deaths"
  }
})
```

Data: The Economist, [covid-19-the-economist-global-excess-deaths-model](https://github.com/TheEconomist/covid-19-the-economist-global-excess-deaths-model)

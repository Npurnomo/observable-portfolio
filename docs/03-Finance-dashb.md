---
theme: dashboard
title: Finance Dashboard 
toc: false
---
# Exploring Financial Dynamics Across Different Industries 

This interactive finance dashboard offers comprehensive insights into various industries in the United States. The data is sourced from Aswath Damodaran's website and meticulously cleaned and processed to create the visualizations. The dashboard includes visualizations that enable users to compare financial metrics across different industries and explore the relationships between them. This endeavor originated from a fundamental curiosity—a genuine interest in unraveling the financial dynamics that differentiate industries.

I embarked on this journey with a quick Google search, only to be disappointed by the lack of an easy way to compare different industries. It was then that I stumbled upon Aswath Damodaran's videos and discovered his website. Inspired by the wealth of information, I decided to create this interactive dashboard to make it easier for others to explore the data and gain insights into the financial landscape of different industries.

Hopefully, this dashboard can serve as a valuable resource for others, providing them with the means to delve into the intricacies of different industries and gain a deeper understanding of their financial characteristics.


```js
const final1 = FileAttachment("data/final.csv").csv({typed: true});
```

```js
function _8(Plot,final1,pickMargin1,pickMargin2,{width}){return(
Plot.plot({
  width,
  color: { legend: false },
  marks: [
    Plot.dot(final1, {
      x: pickMargin1,
      y: pickMargin2,
      fill: "Industry Name",
      tip: true
    })
  ],
  marginLeft: 60
})
)}

function _1(Plot,final1,pickMargin1,{width}){return(
Plot.plot({
  width,
  x: { grid: true },
  y: { grid: true },
  marks: [
    Plot.barY(final1, {
      x: "Industry Name",
      y: pickMargin1,
      fill: "Industry Name",
      tip: true
    }),
    Plot.ruleY([0]),
    Plot.axisX({ticks: []}),
    Plot.ruleX([0])
  ]
})
)}

function _2(Plot,final1,pickMargin2,{width}){return(
Plot.plot({
  width,
  x: { grid: true },
  y: { grid: true },
  marks: [
    Plot.barY(final1, {
      x: "Industry Name",
      y: pickMargin2,
      fill: "Industry Name",
      tip: true
    }),
    Plot.ruleY([0]),
    Plot.axisX({ticks: []}),
    Plot.ruleX([0])
  ]
})
)}
```

```js
const pickMargin1 = view(Inputs.select(
    Object.keys(final1[0]).filter(
      (d) => !["Industry Name", "Number of Firms", "Number of firms_y", "Number of firms_x"].includes(d)
    ),
    {
      label: "Select first metric"
    }
  )
);

```

```js
const pickMargin2 = view(Inputs.select(
    Object.keys(final1[0]).filter(
      (d) => !["Industry Name", "Number of Firms", "Number of firms_y", "Number of firms_x"].includes(d)
    ),
    {
      value: "Buybacks in $ millions",
      label: "Select second metric"
    }
  )
);

```

<div class="card">${pickMargin1} across the industries ${resize((width) => _1(Plot,final1,pickMargin1,{width}))}
</div>
<div class="card">${pickMargin2} across the industries ${resize((width) => _2(Plot,final1,pickMargin2,{width}))}
</div>

<div class="grid grid-cols-1">
  <div class="card">${pickMargin1} on the X axis and ${pickMargin2} on the Y axis ${resize((width) => _8(Plot,final1,pickMargin1,pickMargin2,{width}))}
  </div>
</div>


Data: Aswath Damodoran, [data from 01/2024](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html)

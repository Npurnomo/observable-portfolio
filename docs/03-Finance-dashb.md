---
theme: dashboard
title: Finance dashboard 
toc: false
---
# FINANCE!!!  🚀
<!-- Load and transform the data -->

```js
const final1 = FileAttachment("data/final.csv").csv({typed: true});
```

```js
function _8(Plot,final1,pickMargin1,pickMargin2,{width}){return(
Plot.plot({
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
```

```js
const pickMargin1 = view(Inputs.select(
    Object.keys(final1[0]).filter(
      (d) => !["Industry Name", "Number of Firms", "Number of firms_y", "Number of firms_x"].includes(d)
    ),
    {
      label: "Select X"
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
      label: "Select Y"
    }
  )
);

```



<div class="grid grid-cols-1">
  <div class="card">${resize((width) => _8(Plot,final1,pickMargin1,pickMargin2,{width}))}</div>
</div>
# Remember COVID-19 ?

Showing Covid Time Series for **${country}**

This page gives a brief look at how COVID-19 affected different countries. It shows how Datasette and the Observable framework can work together. Our interactive dashboard displays the number of COVID-19 deaths in a country over time. Using simple queries, we show real-time data from 2020 to 2022, giving a historical view of the pandemic.

This interactive display helps understand how COVID-19 changed over time. You can explore and analyze the data to see how the pandemic affected different places.


```js echo
const country = view(Inputs.select(countries, {
  value: "Albania",
  label: "Country : "
}));
```

```js echo
Plot.plot({
  y: {
    grid: true,
    label: `Time Series of Covid Deaths : ${country}`
  },
  width: width,
  marginLeft: 60,
  marks: [
    Plot.line(data_with_dates, {
      x: "end_date",
      y: "total_deaths",
      title: "Covid Numbers",
      tip: true
    })
  ],
  x: { label: "Date" },
  y: { label: "Number of Deaths" }
})
```

## Fetch data 

```js echo
const country_sql = `select end_date as date, expected_deaths from economist_excess_deaths where country = "${country}" `

```

```js echo
country_sql 

```

```js echo
const data = d3.json(
  `https://covid-19.datasettes.com/covid/economist_excess_deaths.json?country__exact=${country}&_sort_desc=end_date&_shape=array`
);
```



```js echo
const data_with_dates = data.map(function(d) {
  d.end_date = d3.timeParse("%Y-%m-%d")(d.end_date);
  return d;
})
```



```js echo
Inputs.table(data_with_dates)
```
## Fetch list of countries

```js echo
const countriess_sql = "select country from economist_excess_deaths group by country"
```
```js echo
const countries = fetch(
  `https://covid-19.datasettes.com/covid.json?sql=${encodeURIComponent(
    countriess_sql
  )}&_size=max&_shape=arrayfirst`
).then((r) => r.json());
```
```js echo
countries
```

Data: https://covid-19.datasettes.com/covid

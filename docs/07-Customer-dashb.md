---
theme: dashboard
title: SQL Away!!
toc: false
---
# SQL Away through simulated data!

The page is a result of experimenting with a new framework and simulating data at runtime using a JavaScript data loader. The data, stored in a CSV file, is queried using SQL queries through DuckDB. Navigating through different documentation helped me create this page. I aimed for it to be interactive and informative, so I developed a way for visitors to input their SQL queries and view the results in a table format.

```js
const customers = await FileAttachment("data/customer_orders.csv").csv({
  typed: true,
});
```

## Here's data you're working with
```js 
view(Inputs.table(db.query("SELECT * FROM customer_orders.csv")))
```


```js echo
const db = DuckDBClient.of({gaia: FileAttachment("data/customer_orders.csv")});
```
SQL cheat sheet:
- SELECT: extracts data from a database
- WHERE: filters the data
- GROUP BY: groups rows sharing a property
- ORDER BY: sorts the result
- HAVING: filters groups
- LIMIT: limits the number of rows returned


## Your SQL query here
```js echo
const sql = view(Inputs.textarea({value: "SELECT name as NAME, total_pounds as TOTAL FROM customer_orders.csv WHERE number_of_items > 2 ORDER BY TOTAL LIMIT 5", label: "SQL query here:"}))
```

## Your SQL query RESULT

```js echo
Inputs.table(await db.query(sql))
```
## Your histogram here

```js
const column = view(Inputs.select(
    Object.keys(customers[0]).filter(
      (d) => !["id", "name", "country", "email", "device_type"].includes(d)
    ),
    {
      label: "Select your column: "
    }
  )
);
```

```js echo
Plot.plot({
  title: "Histogram of " + column,
  marks: [
    Plot.rectY(customers, Plot.binX({ y: "count" }, { x: column, fill: "aqua" })),
    Plot.ruleY([0])
  ]
})
```

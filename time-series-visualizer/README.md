# [Time Series Visualizer](https://repl.it/@borntofrappe/fcc-time-series-visualizer)

> Third project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

## Assignment

The project asks to visualize a time series with several data visualizations. It is broken down in a series of steps, which I decided to annotate with my solution.

I've included an additional script in `min.py` to ease this incremental development.

### os

This is unrelated to the project, but for local development, the os module allows to point toward the csv file in the current directory.

### Import data

The project adds two details:

1.  parse the dates

    By default pandas reads the column with a type of object. It is only true the appropriate keyword argument that the column(s) is parsed with the desired data type.

    ```py
    df = pd.read_csv(dir + '/' + 'data.csv', parse_dates=["date"])
    print(df.dtypes)
    """
    date     datetime64[ns]
    value             int64
    dtype: object
    """
    ```

2.  use the date column for the index of the dataframe

    The docs specify the `index_col` keyword argument.

    ```py
    df = pd.read_csv(dir + '/' + 'data.csv', index_col="date", parse_dates=["date"])
    print(df.head())
    """
                value
    date
    2016-05-09   1201
    2016-05-10   2329
    2016-05-11   1716
    2016-05-12  10539
    2016-05-13   6933
    """
    ```

### Clean data

Clean the data by filtering out days when the page views were in the top or bottom 2.5%.

The `quantile` function allows to specify the desired thresholds.

```py
lower_threshold = df["value"].quantile(0.025)
upper_threshold = df["value"].quantile(0.975)
print(lower_threshold) # 17876.4
print(upper_threshold) # 177613.075
```

To clean the data, use the `&` and operator to consider the values which are in the `[lower_threshold, upper_threshold]` range.

```py
df_clean = df[(df["value"] > lower_threshold) &
              (df["value"] < upper_threshold)]
print(len(df)) # 1304
print(len(df_clean)) # 1238
```

## Docs

Docs and resources which aided the development of the project.

- [pandas read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

- [pandas quantile](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.quantile.html)

---

- Create a `draw_line_plot` function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be "Daily freeCodeCamp Forum Page Views 5/2016-12/2019". The label on the x axis should be "Date" and the label on the y axis should be "Page Views".
- Create a `draw_bar_plot` function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of "Months". On the chart, the label on the x axis should be "Years" and the label on the y axis should be "Average Page Views".
- Create a `draw_box_plot` function that uses Searborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)". Make sure the month labels on bottom start at "Jan" and the x and x axis are labeled correctly.

For each chart, make sure to use a copy of the data frame. Unit tests are written for you under `test_module.py`.

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

### Line plot

Map the values with a line plot. The title should be "Daily freeCodeCamp Forum Page Views 5/2016-12/2019". The label on the x axis should be "Date" and the label on the y axis should be "Page Views".

seaborn provides the `lineplot` function, which handily plots the time series by specifying the `x` and `y` keyword arguments.

Start by setting up a figure with matplotlib

```py
fig = plt.figure(figsize=(16, 5))
```

Plot the data with seaborn, and keep a reference to the ax in which the visualization is created

```py
ax = sns.lineplot(x=df_clean.index, y=df_clean["value"])
```

In this manner, you can update the title and axes' labels with the `.set()` function. Individually:

```py
ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
ax.set_xlabel("Date")
ax.set_ylabel("Page Views")
```

Or with a single `.set` describing the values through keyword arguments.

```py
ax.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views")
```

### Bar chart

Map the values with a bar chart. Show average daily page views for each month, and group the columns by year. The legend should show month labels and have a title of "Months". For the chart, the label on the x axis should be "Years" and the label on the y axis should be "Average Page Views".

Creating the bar chart took a lot of trial and error. Ultimately, I found a couple of different ways to create the same plot, and I'd like to detail both for posterity's sake.

#### Copy

Start by copying the dataframe, to avoid altering the original one.

```py
df_copy = df_clean.copy()
```

#### Group

The visualization needs to plot one bar for each month. To group the observations by month, use `pd.Grouper`. The function allows to resample the observations with a given frequency. In this instance, on a monthly basis.

```py
df_group = df_copy.groupby(pd.Grouper(freq="M"))
```

You can achieve a similar result using a list and the index column.

```py
df_group = df_copy.groupby([df_copy.index.year, df_copy.index.month])
```

However, this introduces a new hurdle in that the index column is no longer represented by a DatetimeIndex, but a MultiIndex.

In the first instance the index is represented by a list of dates (`['2016-05-31', '2016-06-30', '2016-07-31', '2016-08-31'...`). In the second instance, by a list of tuples (`(2016, 5), (2016, 6), (2016, 7), (2016, 8),`).

To later add a column for the year and month, it is more convenient to keep the date syntax.

That being said, once the dataframe is "grouped", so to speak, you can highlight the groups using the `.head()` function.

```py
print(df_group.head(1))
"""
             value
date
2016-05-19   19736
2016-06-07   18335
2016-07-01   28372
"""
```

Notice how the `head()` method is not showing the elements at the top of the dataframe, but the elements at the top _of every group_: may 2016, june 2016, and so forth.

Operations like `sum` now work on a group level instead of considering the entire dataframe. In other words, if `df_clean.sum()` would tally all the values, `df_group.sum()` would do so for the values of groups, distinctly.

```py
print(df_clean.sum())
"""
value    78068463
dtype: int64
"""
print(df_group.sum())
"""
              value
date
2016-05-31    97162
2016-06-30   415627
2016-07-31   675071
2016-08-31   962525
2016-09-30  1244306
...
"""
```

`sum`, or in the instance of the project, `mean` to compute the average.

```py
df_bar = df_group.mean()
print(df_bar)
"""
                    value
date
2016-05-31   19432.400000
2016-06-30   21875.105263
2016-07-31   24109.678571
2016-08-31   31049.193548
2016-09-30   41476.866667
"""
```

That bar chart needs to distinguish the observations on the basis of the month (for the colo), and year (for the position on the `x` axis).

From the grouped dataframe, you can do so using the `index`, or, alternatively, specifying a column for the date object itself.

#### Datetime index

Using the index, you can add the year value and the name of the month using the following syntax.

```py
df_bar["month"] = df_bar.index.month_name()
df_bar["year"] = df_bar.index.year
print(df_bar.head(2))
"""
                   value month  year
date
2016-05-31  19432.400000   May  2016
2016-06-30  21875.105263  June  2016
"""
```

#### date column (alternative)

Without using the `index`, you can actually create a dataframe in which the date is represented in its own column.

```py
df_bar = df_bar.reset_index()
print(df_bar.head(2))
"""
        date         value
0 2016-05-31  19432.400000
1 2016-06-30  21875.105263
"""
```

The year and month can be then included using the `dt.strftime` construct provided by the pandas library

```py
df_bar["month"] = df_bar["date"].dt.strftime("%B")
df_bar["year"] = df_bar["date"].dt.strftime("%Y")
"""
        date         value month  year
0 2016-05-31  19432.400000   May  2016
1 2016-06-30  21875.105263  June  2016
"""
```

As you can see, the dataframe is eerily similar. You just need to pay attention that the `date` is represented as in the index, or in its own column.

#### barplot

With the dataframe now describing the desired structure, seaborn plots a bar plot through the `barplot` function.

```py
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

fig = plt.figure(figsize=(10, 8))

# bar plot

fig.savefig(dir + '/' + './bar_plot.png')
```

`months` is included to specify the order of the legend and the order in which the bar are positioned. The rest of the code sets up a figure, which is then saved locally.

For the bar plot, specify the appearance of the plot through its several, foundational attributes:

```py
sns.barplot(x="year", y="value", hue="month", hue_order=months, data=df_bar)
```

From the left:

- `x="year"` allows to separate the visualization horizontally and according to the year value.

- `y="value"` details the height of the bars

- `hue="month"` makes it possible to distinguish the bar according to the color. Color which is associated to the month value

- `hue_order=months` allows to have the bars, and the legend, start with January and end in December. Without its mention, the first month would be May, since this is the value for the first data point.

This takes care of the bar plot. To change the appearance of the axes & legend, keep a reference to the current ax by storing the return value of the `barplot` function.

```py
ax = sns.barplot()
```

From this ax, you can change the axes and legend with the associated function.

```py
ax.set(xlabel="Years", ylabel="Average Page Views")
ax.legend(title="Months", loc="upper left")
```

### Box plot

Draw two adjacent box plots, to show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)". Make sure the month labels on bottom start at "Jan" and the axes are labeled correctly.

## Docs

Docs and resources which aided the development of the project.

- [pandas read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

- [pandas quantile](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.quantile.html)

- [pandas grouper](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html)

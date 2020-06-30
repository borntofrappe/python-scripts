# [Time Series Visualizer](https://repl.it/@borntofrappe/fcc-time-series-visualizer)

> Third project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

## Assignment

The project asks to take the `.csv` data describing traffic to the freeCodeCamp forum, between May 2016 and December 2019, and map the time series with a line chart, a bar chart and a box plot. Each visualization has its own distinct merit, be it the analysis of the growth, of the averages, of the trends.

## Development

`main.py` is the entry point for the script. Once run, it will take the code from `visualizer.py` and run the three functions to produce the desired visualization in the form of `.png` images.

`min.py` is a file I personally added to explore the pandas and seaborn library.

## Notes

A few things I"ve learned from the script, about pandas, seaborn, matplotlib and anything in between. Each section is introduced with a few keywords, and ends with links for more information.

### os

> path, dirname, **file**

This section is included only for the project as developed locally. In the online REPL, it is possible to read and save files using relative paths.

```py
df = pd.read_csv("data.csv")

fig.savefig("plot.png")
```

Locally, however, I find it necessaryto describe the absolute path. With this regard, the `os` module helps to find the path to the current directory. Most precisely, the directory of the python script which is run. `main.py` or `min.py` .

```py
import os

dir = os.path.dirname(__file__)
df = pd.read_csv(dir + "/data.csv")

fig.savefig(dir + "/plot.png")
```

`__file__` describes the absolute path for the file being run: `C:/python/python-scripts/time-series-visualizers/min.py`

`os.path.dirname` strips the string of the file to return the directory `C:/python/python-scripts/time-series-visualizers`

A stackoverflow answer seems to add the `os.path.realpath` function, to returns the "canonical" path

```py
dir = os.path.dirname(os.path.realpath(__file__))
```

However, and for the project at hand, it seems superfluous. As I understand the method, it allows to have describe the path with a specific format, in a specific standard. This _canonical_ standard makes it possible to compare two different paths, no matter how they are structure. For instance, and again as I understand it, it allows to compare two paths like the following (as long as `..` and `folder` describe the same location).

```code
../file
folder/file
```

Since the project is interested in just reading/saving files to the directory, it seems less than necessary to include the step.

##### Docs

- [os module](https://docs.python.org/3/library/os.html)

- [stackoverflow on finding the current directory](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjEuYbvgqnqAhUwxMQBHcgbCjUQFjAAegQIAxAB&url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F5137497%2Ffind-current-directory-and-files-directory&usg=AOvVaw17mJeQBbfPchjQ4_ratVQ6)

- [stackoverflow on canonical paths](https://stackoverflow.com/questions/12100299/whats-a-canonical-path)

### Import data

> read_csv, parse_dates

Given a source file in `data.csv`, the pandas library builds a dataframe with the `read_csv` function.

```py
import pandas as pd

df = pd.read_csv(dir + "/data.csv")
```

As instructed in the project however, the dataframe is built with two modifications:

- parse the dates in the `date` column

  By default, the column is interpreted with a type of `object`

  ```py
  print(df["date"].dtype)
  """
  object
  """
  ```

  The `parse_dates` argument allows to have the values as a Datetime object.

  ```py
  df = pd.read_csv(dir + "/data.csv", parse_dates=["date"])
  print(df["date"].dtype)
  """
  datetime64[ns]
  """
  ```

  This will come in handy to later retrieve the month, year, and other features of the date.

  ```py
  print(df["date"][0].year)
  """
  2016
  """
  ```

- use the dates in the `date` column for the index of the dataframe.

  By default the dataframe uses integers.

  ```py
  print(df.index)
  """
  RangeIndex(start=0, stop=1304, step=1)
  """
  ```

  The `index_col` argument allows to use whichever column.

  ```py
  df = pd.read_csv(dir + "/data.csv", parse_dates=["date"], index_col="date")

  print(df.index)
  """
  DatetimeIndex(['2016-05-09', '2016-05-10', '2016-05-11', '2016-05-12', '2016-05-13', '2016-05-14',
  ],
  dtype='datetime64[ns]', name='date', length=1304, freq=None)
  """
  ```

The dataframe now describes the data as follows:

```py
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

The projects asks to remove the values exceeding a given range: below the 2.5th, and above the 97.5th percentile.

The `quantile` function determines this values specifying a float in the `[0,1]` range

```py
lower_threshold = df["value"].quantile(0.025)
upper_threshold = df["value"].quantile(0.975)
```

The dataframe can be then updated to consider the desired range using different operators. For instance and using the `&` and operator.

```py
df = df[(df["value"] > lower_threshold) & (df["value"] < upper_threshold)]
```

Using the `len` function you can see that the dataframe changes in length.

```py
print(len(df)) # 1304
df = df[(df["value"] ...

print(len(df)) # 1238
```

Doesn't prove that the structure changed by removing the smallest/greatest values. This is something you can glance at using the `describe` function.

```py
print(df.describe())
"""
min    1.201000e+03
max    1.173655e+06
"""
df = df[(df["value"] ...

print(df.describe())
"""
min     18060.000000
max    177588.00000
"""
```

I've noted the `min` and `max` values to illustrate the point.

### Line chart

The first visualization is a line chart. Using seaborn and the `lineplot` function, data is mapped describing the values of the `x` and `y` axes using the corresponding arguments.

```py
import seaborn as sns

sns.lineplot(x=df.index, y=df_clean["value"])
```

This would be enough to show the line in a jupyter notebook. However, to create the chart locally, and to also have more control on the aesthetics of the visualization, it is necessary to use matplotlib.

```py
import matplotlib.pyplot as plt

fig_line = plt.figure(figsize=(15, 5))

sns.lineplot(x=df.index, y=df["value"])

fig_line.savefig(dir + "/line_plot.png")
```

The seaborn function operates on the current ax, and in the figure created by matplotlib.

To change the title of the line chart, and the labels included on either axis, you can leverage the fact that `sns.lineplot` returns the ax on which the visualization is created.

```py
ax_line = sns.lineplot()
```

Ax which can be updated in appearance using the `set` function.

```py
ax_line.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views")
```

You can also change the features individually

```py
ax_line.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
ax_line.set_xlabel("Date")
ax_line.set_ylabel("Page Views")
```

### Bar chart

```py

```

```py

```

<!--

### Bar chart

Map the values with a bar chart. Show average daily page views for each month, and group the columns by year. The legend should show month labels and have a title of "Months". For the chart, the label on the x axis should be "Years" and the label on the y axis should be "Average Page Views".

Creating the bar chart took a lot of trial and error. Ultimately, I found a couple of different ways to create the same plot, and I"d like to detail both for posterity"s sake.

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

In the first instance the index is represented by a list of dates (`["2016-05-31", "2016-06-30", "2016-07-31", "2016-08-31"...`). In the second instance, by a list of tuples (`(2016, 5), (2016, 6), (2016, 7), (2016, 8),`).

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
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

fig = plt.figure(figsize=(10, 8))

# bar plot

fig.savefig(dir + "/" + "./bar_plot.png")
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

- [pandas grouper](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html) -->

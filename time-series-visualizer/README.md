# [Time Series Visualizer](https://repl.it/@borntofrappe/fcc-time-series-visualizer)

> Third project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

## Assignment

The project asks to take the `.csv` data describing traffic to the freeCodeCamp forum, between May 2016 and December 2019, and map the time series with a line plot, a bar plot and a box plot. Each visualization has its own distinct merit, be it the analysis of the growth, of the averages, of the trends.

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

##### Reference

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

#### Reference

- [pandas on read_csv](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)

### Clean data

> quantile

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

### Line plot

> lineplot, figure, ax

The first visualization is a line plot. Using seaborn and the `lineplot` function, data is mapped describing the values of the `x` and `y` axes using the corresponding arguments.

```py
import seaborn as sns

sns.lineplot(x=df.index, y=df_clean["value"])
```

This would be enough to show the line in a jupyter notebook. However, to create the plot locally, and to also have more control on the aesthetics of the visualization, it is necessary to use matplotlib.

```py
import matplotlib.pyplot as plt

fig_line = plt.figure(figsize=(15, 5))

sns.lineplot(x=df.index, y=df["value"])

fig_line.savefig(dir + "/line_plot.png")
```

The seaborn function operates on the current ax, and in the figure created by matplotlib.

To change the title of the line plot, and the labels included on either axis, you can leverage the fact that `sns.lineplot` returns the ax on which the visualization is created.

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

#### Reference

- [seaborn on lineplot](http://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot)

### Bar plot

> groupby, barplot

The second visualization is a bar plot, plotting the monhtly averages and separating the observations horizontally according to the year.

It is necessary to group the dataframe according to the desired timeframe (month), but the project asks first to create a copy of the dataframe. This is most likely to avoid modifying the original `df`

```py
df_bar = df.copy()
```

To group the data according to the month, use the `Grouper` function.

```py
df_bar = df_bar.groupby(pd.Grouper(freq="M"))
```

Once the dataframe is "grouped", so to speak, you can highlight the groups using the `.head()` function.

```py
print(df_bar.head(1))
"""
             value
date
2016-05-19   19736
2016-06-07   18335
2016-07-01   28372
2016-08-01   20947
...
"""
```

Notice how the `head()` method is not showing the elements at the top of the dataframe, but the elements at the top _of every group_: may 2016, june 2016, and so forth.

Operations like `sum` and `mean` now work on a group level instead of considering the entire dataframe. In other words, if `df.mean()` would consider all the values, `df_bar.mean()` would do so for the values of groups, distinctly.

```py
print(df.mean())
"""
value    63060.147819
dtype: float64
"""

df_bar = df_bar.mean()
print(df_bar)
"""
                    value
date
2016-05-31   19432.400000
2016-06-30   21875.105263
2016-07-31   24109.678571
2016-08-31   31049.193548
...
"""
```

This takes care of computing the averages for the month and year. It is however necessary to add two columns, to describe the month and year value separately. This is necessary to later have seaborn change the position, and color, of the bars depending on the precise values.

You can actually achieve this in one of two ways.

1. use the index

   ```py
   df_bar["month"] = df_bar.index.month_name()
   df_bar["year"] = df_bar.index.year
   ```

   Since the index describes object of type date, you can describe its features with the `.year` attribute and `month_name()` function. This last one returns the full name of the month.

2. reset the index and use the value of the `date` column


    ```py
    df_bar = df_bar.reset_index()
    df_bar["month"] = df_bar["date"].dt.strftime("%B")
    df_bar["year"] = df_bar["date"].dt.strftime("%Y")
    ```

    The `.dt.strftime`, while more cryptic, allows to create the same values specifying the month name, `%B` and for digit year, `%Y`.

    I consider this a more "radical" approach, as it modifies the structure of the dataframe. The index is now and again a `RangeIndex`.

The approaches lead a similar outcome: the dataframe has now a column for the month and one column for the year. These are included in the `barplot` function.

```py
sns.barplot(x="year", y="value", hue="month", data=df_bar)
```

Similarly to the line plot, a few more lines are necessary to produce the file locally.

```py
fig_bar = plt.figure(figsize=(10, 8))

sns.barplot()

fig_bar.savefig(dir + "/bar_plot.png")
```

Again, and similarly to the line plot, `barplot` returns the current ax. This can be used to modify the labels of the bar plot, but also the legend, to comply with the assignment and its requirements.

```py
ax_bar = sns.barplot()

ax_bar.set(xlabel="Years", ylabel="Average Page Views")
ax_bar.legend(title="Months", loc="upper left")
```

One last note however: in its current rendition, the bar plot maps data in a rather undesired order. Indeed, the months start at may, to end at april. This is because the first observation is for May 2016.

To change this default, create a list for the names of the months, and use this list in the `hue_order` argument of the seaborn function.

```py
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

sns.barplot(x="year", y="value", hue="month", hue_order=months, data=df_bar)
```

#### Reference

- [pandas on grouper](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html)

- [seaborn on barplot](https://seaborn.pydata.org/generated/seaborn.barplot.html)

### Box plot

> groupby, boxplot, list comprehension

The third visualizaton is a box plot, or rather two box plot, side by side.

The idea is to describe the values on a yearly and monthly basis, which means the dataframe mirrors much of the instructions specified for the bar plot.

```py
df_box = df.copy()
df_box["month"] = df_box.index.month_name()
df_box["year"] = df_box.index.year
```

From this structure, `boxplot` allows to create the desired visualization specifying the `x` and `y` arguments.

For the years:

```py
sns.boxplot(x="year", y="value", data=df_box)
```

For the months, again with the desired order starting at January:

```py
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

sns.boxplot(x="month", y="value", order=months, data=df_box)
```

This is enough to highlight the boxplot in a jupyter notebook,but as with the previous visualizations, matplotlib allows to recreate the plot locally.

Unlike the previous visualizations, however, it is necessary to create a figure with two subplots.

```py
fig_box, axs_box = plt.subplots(1, 2, figsize=(17, 5))
ax1, ax2 = axs_box

# viz

fig_box.savefig(dir + "/box_plot.png")
```

`subplots` describes a figure with one row and two columns. `ax1` and `ax2` can be then used to include the visualization in either subplot.

The `boxplot` function accepts an additional argument in `ax`, which aptly links to the ax in which to plot the data.

```py
sns.boxplot(..., ax=ax1)
sns.boxplot(..., ax=ax2)
```

`ax1` and `ax2` can be used to also modify the title/labels of either visualization. Exactly like in the previous instances.

One last note is for the labels included on the `x` axis of the secon boxplot. Instead of showing the name of the month in full, the idea is to show only the first three letters (Jan instead of January, Feb, and so forth). The `xticklabels` argument allows to modify the default value, with a list of the same length.

```py
xticklabels=[m[:3] for m in months]
```

Using a list comprehension which is syntactic sugar for:

```py
mon = []
for m in months:
    mon.append(m[:3])
```

Using slicing notation to consider every character up to the third index (not included).

#### Reference

- [seaborn on boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html)

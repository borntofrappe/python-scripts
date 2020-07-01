# [Sea level predictor](https://repl.it/@borntofrappe/fcc-sea-level-predictor)

> Fifth project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

## Assignment

The project asks to take the data from `data.csv`, which describes the level of sea rise between 1880 and 2013, plot a few visualizations and predict the change occurring between 2013 and 2050.

This using the following libraries:

- pandas, to read and manipulate the data

- matplotlib, to plot the data

- scipy, to predict the level within an error margin

## Development

`main.py` is the entry point for the script. Once run, it will take the code from `predictor.py` and run the functions to produce the desired visualization in the form of `.png` images.

`min.py` is a file I personally added to explore the libraries and build the project in increments.

## Notes

A few things I've learned developing the script.

### Import data

Similarly to the other projects for the same certification, use pandas and the `read_csv` function to create a dataframe from `data.csv`. Take advantage of the `os` module to describe the path to the data file.

```py
import pandas as pd
import os

dir = os.path.dirname(__file__)

df = pd.read_csv(dir + '/data.csv')
print(df.head())
"""
   Year  CSIRO Adjusted Sea Level  Lower Error Bound  Upper Error Bound  NOAA Adjusted Sea Level
0  1880                  0.000000          -0.952756           0.952756                      NaN
1  1881                  0.220472          -0.732283           1.173228                      NaN
2  1882                 -0.440945          -1.346457           0.464567                      NaN
3  1883                 -0.232283          -1.129921           0.665354                      NaN
4  1884                  0.590551          -0.283465           1.464567                      NaN
"""
```

It's interesting to see how the last column has `NaN` values. Looking at the length of the dataframe vis-a-vis the number of `NaN` values, it seems that `NaN` values represent the majority of the column.

```py
print(len(df)) # 134
print(df["NOAA Adjusted Sea Level"].isna().sum()) # 113
```

### Scatter plot

The idea is to use matplotlib to map the data according to the `year` and `CSIRO Adjusted Sea Level` columns.

Looking at the starter code from `predictor.py`, it seems the script asks to use the library through its global interface.

```py
import matplotlib.pyplot as plt

plt.savefig('sea_level_plot.png')
```

In other words, you use the `plt` object to create the data visualizations, and modify the global object instead of creating separate interfaces.

For the data visualization, `scatter` accepts as argument the dimensions of the scatter plot:

```py
plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
```

I've added labels and a title to comply with the assignment, but that covers the scatter plot.

```py
plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
```

#### Resources

- [matplotlib on the `.scatter` function](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html)

### Line of best fit

Using the `scipy` library and the `linregress` function, the project asks to compute the slope and y-intercept of the _line of best fit_.

```py
regression = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
print(regression)
"""
LinregressResult(slope=0.06304458401213482, intercept=-119.06594196773983, rvalue=0.9847571311825853, pvalue=3.788696979107662e-102, stderr=0.000969211871328706)
"""
```

With this information, the assignment is to then plot the line on top of the scatter plot, and for values in the `1880-2050` range.

```py
slope, intercept, rvalue, pvalue, stderr = linregress(
    df["Year"], df["CSIRO Adjusted Sea Level"])

x1 = df["Year"][0]
x2 = 2050
y1 = intercept + x0 * slope
y2 = intercept + x1 * slope

plt.plot([x1, x2], [y1, y2])
```

The line shares the same color of the scatter plot, but with a few more arguments it is made more evident.

```py
plt.plot([x1, x2], [y1, y2], linewidth=2, color="red")
```

It is also not required by the assignment, but I've added a legend with a label describing the purpose of the line.

```py
plt.plot([x1, x2], [y1, y2], linewidth=2, color="red", label="Line of best fit")
plt.legend()
```

#### Resources

- [scipy tutorial on `scipy.stats`](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)

- [scipy docs for `linregress`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html)

- [matplotlib on line charts with `plot`](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html)

### Line of best fit/2

The final request of the assignment is to plot yet another line of best fit, considering a subset of the original data, and more specifically starting with the year 2000.

```py
df_2000 = df[df["Year"] >= 2000]
```

With the new column, it is a matter of repeating the computations used for the first line chart. However, one modification is with the way `x1` is computed. It is actually valid for the first line as well: using the previous syntax

```py
x1 = df["Year"][0]
```

Works only because the data point at the `0`th index happens to be the first value. In the modified dataframe. however, there is no `0`th index. To pick the first item based on position and not index, use the `iloc()` function.

```py
x1 = df.iloc[0]["Year"]
```

There's a minor issue in that the value is returned as a float, but to fix this, wrap the result in the `int` function.

```py
x1 = int(df.iloc[0]["Year"])
```

It doesn't change the way the line(s) are plotted, but in the moment the years are included in the legend (as they are), it makes a difference.

```py
label="Line of best fit " + str(x1) + "-" + str(x2)
```

With this in mind, the new line of best fit repeats the exact same computations and the exact same function to plot the line. The only difference relates to the color, to differentiate the two.

#### Reference

- [pandas iloc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html)

### Debugging

Running the script against the testing suite raises the following error:

```bash
Traceback (most recent call last):
  File "/home/runner/fcc-sea-level-predictor/test_module.py", line 34, in test_plot_lines
    self.assertEqual(actual, expected, "Expected different line for first line of best fit.")
AssertionError: Lists differ: [-0.5421240249263661, 10.175455257136548] != [-0.5421240249263661, -0.4790794409142336, -0.41603485690208686[3235 chars]2443]
```

In its rather convoluted syntax, the message points to the `test_plot_lines` in `test_module.py`, where the function compares a series of variables against hard-coded values. The message points specifically to the coordinates of the line of best fit, as returned by the syntax `ax.get_lines()[0].get_ydata().tolist()`.

Considering it one step at a time:

- `ax.get_lines()` returns a list of the lines mapped the ax

  ```py
  ax = sea_level_predictor.draw_plot()

  lines = ax.get_lines()
  print(lines)
  """
  <a list of 2 Line2D objects>
  """
  ```

  `lines[0]` refers to the first line, detailing the `Line2D(Line of best fit 1880-2050)` object

- the `.get_ydata()` function returns a list of the coordinates on the `y` axis

  ```py
  ydata = lines[0].get_ydata()
  print(ydata)
  """
  [-0.54212402 10.17545526]
  """
  ```

  You might already see the problem, but first, to finish the syntax of the test

- `.tolist()` returns the data in a list structure

  ```py
  print(ydata.tolist())
  """
  [-0.5421240249263661, 10.175455257136548]
  """
  ```

Comparing the list to the hard-coded one, the error becomes obvious.

```py
expected = [-0.5421240249263661, -0.4790794409142336, -0.41603485690208686, -0.3529902728899543, -0.2899456888778218, -0.22690110486568926, -0.16385652085355673, -0.1008119368414242,
...]
```

The line is plotted using only two points, while the test considers one point for each year in the `1880-2050` range. It's not an inherent problem with the visualization, and more of a different way to draw the same chart.

Instead of using two points:

```py
x1 = int(df.iloc[0]["Year"])
x2 = 2050
y1 = intercept + x1 * slope
y2 = intercept + x2 * slope
```

Build two lists for the values in the`x` and `y` dimensions.

```py
x = [year + x1 for year in range(x2 - x1)]
y = [intercept + year * slope for year in x]
```

I've used a list comprehensions as a syntactic sugar, but you can achieve a similar result as follows:

```py
x = []
for year in range(x2 - x1):
  x.append(year + x1)

y = []
for year in x:
  y.append(intercept + year * slope)
```

With the data structures, the line is then plotted as follows:

```py
plt.plot(x, y)
```

**One key difference**: the new method maps data in the `1880-2050` range, excluding the year `2050`. It seems this is exactly what the test expects, as the last value in the hard coded array matches the value for `2049`.

| Year | Value              |
| ---- | ------------------ |
| 2049 | 10.11241067312443  |
| 2050 | 10.175455257136548 |

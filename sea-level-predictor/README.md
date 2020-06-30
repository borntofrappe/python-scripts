# Sea level predictor

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
df_recent = df[df["Year"] >= 2000]
```

With the new column, it is a matter of repeating the computations used for the first line chart. However, one modification is with the way `x1` is computed. It is actually valid for the first line as well: using the previous syntax

```py
x1 = df["Year"][0]
```

Works only because the data point at the `0`th index happens to be the first value. In the modified dataframe. however, there is no `0`th index. To pick the first item based on position and not index, use the `iloc()` function.

```py
x1 = int(df.iloc[0]["Year"])
```

With this in mind, the new line of best fit repeats the exact same computations and the exact same function to plot the line. The only difference relates to the color, to differentiate the two.

##### Reference

- [pandas iloc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html)

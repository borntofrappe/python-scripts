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

x0 = df["Year"][0]
x1 = 2050
y0 = intercept + x0 * slope
y1 = intercept + x1 * slope

plt.plot([x0, x1], [y0, y1])
```

The line shares the same color of the scatter plot, but with a few more arguments it is made more evident.

```py
plt.plot([x0, x1], [y0, y1], linewidth=2, color="red")
```

It is also not required by the assignment, but I've added a legend with a label describing the purpose of the line.

```py
plt.plot([x0, x1], [y0, y1], linewidth=2, color="red", label="Line of best fit")
plt.legend()
```

#### Resources

- [scipy tutorial on `scipy.stats`](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html)

- [scipy docs for `linregress`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html)

- [matplotlib on line charts with `plot`](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html)

<!--
*
* Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
* The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".

Unit tests are written for you under `test_module.py`.

### Development

For development, you can use `main.py` to test your functions. Click the "run" button and `main.py` will run.

### Testing

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

### Data Source
Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.
https://datahub.io/core/sea-level-rise

-->

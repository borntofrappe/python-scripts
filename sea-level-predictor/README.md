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

I've added labels and a title, but this is not necessary to complete the project.

```py
plt.title("Sea Level Rise")
plt.xlabel("Year")
plt.ylabel("Adjusted Sea Level")
```

#### Resources

- [matplotlib on the `.scatter` function](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html)

---

<!--
* Use the `linregress` function from `scipi.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
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

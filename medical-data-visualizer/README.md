# [Medical Data Visualizer](https://repl.it/@borntofrappe/fcc-medical-data-visualizer)

> Third project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

Just like with the project **demographic-data-analyzer**, there is a `.csv` file describing the data, and this stores a subset of the original source data.

I've added two more files than actually necessary:

- `min.py`. `main.py` is structured to comply with freeCodeCamp testing suite, but it allows for less experimentation. With `min.py` I tried my luck with the pandas and seaborn library without considering the initial requirements.

- `.gitignore`. This additional gitignore file is added to disregard the `.png` images produced by the script. I feel the output is less important than the script producing it, and the images would pollute the repository.

## Assignment

The project asks to create data visualizations to highlight the medical data found in `data.csv`. In details, it asks to go through a series of steps, which I'll describe alongside the necessary code.

### Overweight column

> Add an 'overweight' column, where an overweight person is described with a value of `1`, and an otherwise not overweight person with a value of `0`.

Being overweight is determined by the weight and height of each person, and particularly by the relationship `weight / (height ^ 2)`. This value is the Body Mass Index (BMI), and highlights an overweight character with a measurement greater than `25`.

It is important to stress the unit of measure of this value: `kg/m^2`. This means the weight must be in kilograms, the height in meters. The `weight` column already describes the weight in kilograms, but the `height` column provides the height in centimeters.

The step asks to assign values of `1` and `0`, but personally, I found it easier to use the weight and height column to assign a boolean.

```py
df["overweight"] = df["weight"] / ((df["height"] / 100) ** 2) > 25
```

Here the overweight column is created and populated with `True` or `False` values, describing whether a person is overweight or not.

With a boolean, I can then update the values with the `.replace` function.

```py
df["overweight"].replace({False: 0, True: 1})
```

Paying attention that this does not modify the original data structure, but returns a new data frame.

### Normalized data

> normalize the columns to repeat the same convention introduced with the overweight column. In this light, a value `0` has a positive connotation, while a value of `1` casts a negative shade.

The project details the `cholesterol` and `gluc` columns. These have multiple values, but the idea is to normalize these values with `1`s and `0`s.

| Value | Connotation | Normalized |
| ----- | ----------- | ---------- |
| =1    | Good        | 0          |
| >1    | Bad         | 1          |

This is where the previous step of assigning a boolean comes in handy. The idea is to reassign the two columns with `True` and `False` values.

```py
df["cholesterol"] = df["cholesterol"] > 1
df["gluc"] = df["gluc"] > 1
```

And then apply the `replace` function not on the `overweight` column only, but on the entire dataframe.

```py
df.replace({False: 0, True: 1})
```

### Long format

> convert the data into long format

Researching the seaborn library, I've come to understand long format as having one observation for each desired variable. In other words, instead of having the data structured as in the following short (wide format):

```code
cholesterol  gluc  smoke  alco  active  cardio  overweight
0            0     0      0     1       0       0
1            0     0      0     1       1       1
1            0     0      0     0       1       0
...
```

You repeat the values for each individual column (hence the long format)

```code
variable value
```

For instance, and for a few observations:

```code
variable value
cholesterol 0
cholesterol 1
cholesterol 1
gluc 0
gluc 0
gluc 0
...
```

Understanding the long format, the operation is achieved with the `melt` function. Provided by the `pandas` library, is specifies the columns which need to be "elongated" in the `value_vars` argument.

```py
df_long = pd.melt(df_normal, value_vars=[
                  "active", "alco", "cholesterol", "gluc", "overweight", "smoke"])
```

Since the observations need to be differentiated on the basis of the `cardio` property, it is also necessary to consider the matching column; this is achieved with the `id_vars` argument.

```py
pd.melt(df_normal, id_vars="cardio", value_vars=[...])
```

### Bar chart

> create a chart that shows the value counts of the categorical features using seaborn's `catplot()`.

In more details, the project asks to split the data according to the values in the 'cardio' column (`0`s and `1`s here as well). The idea is to have two adjacent bar charts, one for each value.

Split by cardio, you should highlight the count, the number of observation for the following columns:

- active
- alco
- cholesterol
- gluc
- overweight
- smoke

This is achieved with the seaborn library and the `catplot` function, specifying a kind argument of `kind=count`. The idea being that seaborn creates a _countplot_.

With the data in the long format, the function is surprisingly readable.

```py
sns.catplot(x="variable", hue="value", col="cardio", kind="count", data=df_long)
```

`variable` refers to each variable described in the "elongated" format: active, alco and so forth. `value` distinguishes between the variables' own values (`0`s and `1`s). `col` allows to create the two _facets_ of the bar chart.

In a jupyter notebook it is enough to run the function, but to save the function locally you can store the catplot in a variable, and use the `savefig` function specifying the output path.

```py
fig = sns.catplot(...)
fig.savefig("/catplot.png")
```

### Incorrect data

For the correlation matrix, the project asks to filter out the measurement matching the following conditions

- the `ap_lo` column has a value greater than the `ap_hi` column
- the `height` column is below the 2.5th percentile, or greater than the 97.5th one
- the `width` column is below the 2.5th percentile, or greater than the 97.5th one

While the first condition is based on a comparison of the two columns, the second and the third require you to compute the necessary percentiles.

```py
height_low_percentile = df_normal["height"].quantile(0.025)
height_high_percentile = df_normal["height"].quantile(0.975)

weight_low_percentile = df_normal["weight"].quantile(0.025)
weight_high_percentile = df_normal["weight"].quantile(0.975)
```

To consider only those observations matching the requirements above, I considered a dataframe matching the listed conditions

```py
df_normal[(df["ap_lo"] > df["ap_hi"]) | (df["height"] < height_low_percentile) | (df["height"] > height_high_percentile) | (
    df["weight"] < weight_low_percentile) | (df["weight"] > weight_high_percentile)]
```

And then used the `~` tilde character on the entire set.

```py
df_clean = df_normal[~((df["ap_lo"] > df["ap_hi"]) | (df["height"] < height_low_percentile) | (df["height"] > height_high_percentile) | (
    df["weight"] < weight_low_percentile) | (df["weight"] > weight_high_percentile))]
```

### Correlation matrix

> Plot the correlation matrix using seaborn's `heatmap()`. Mask the upper triangle.

This required a bit of reseach not only for seaborn, but pandas as well.

It is first necessary to plot a correlation matrix. This is done through pandas, and a function made available on every dataframe.

```py
corr = df_heat.corr()
```

This is already enough to plot the heatmap, and with default values.

```py
sns.heatmap(data=corr)
```

However, and for the project, it is necessary to mask the upper right section to effectively show a triangle.

The mask works as follows: a 2d array, matching the shape of the correlation matrix, which is interpreted with `True` and `False` values. For every `True` value, then, the heatmap hides the corresponding square.

To build the mask, it is possible to use the array of values behind `corr.columns` alongside the `triu` function provided by `numpy`.

```py
np.triu(corr.columns)
```

For the `tril` and `triu` functions, numpy builds the desired 2d array, and places `0` past/before the diagonal.

Effectively, it is already possible to use this 2d array filled with strings and `0`s.

```py
mask = np.triu(corr.columns)

"""
[['id' 'age' 'gender' ...]
 [0 'age' 'gender' ...]
 [0 0 'gender' ...]
]
"""
```

The strings are truthy values, and hide the top right section of the matrix.

```py
sns.heatmap(data=corr, mask=mask)
```

And that wraps up the code to complete the assignment. Ultimately, the `heatmap` function includes additional keyword arguments, but these instructions are purely aesthetic:

- add the correlation value in the individual cells: `annot=True, fmt='.1f'
- resize each cell to be a square: `square=True`
- resize the legend to occupy a fraction of the original dimension (by default it matches the height of the matrix): `cbar_kws={'shrink': 0.5}`

### Debugging

The testing suite fails with the following error messages:

1. test_line_plot_labels: 'numpy.ndarray' object has no attribute 'get_xlabel'

2. test_bar_plot_number_of_bars: 'numpy.ndarray' object has no attribute 'get_children'

They are both connected to the catplot function, and looking at the testing code, they are both connected to the `ax` object. This is retrieved as `self.fig.axes[0]`, where `self` refers to the figure returned by the catplot function. In the first instance, the attribute should return the string `variable`, for the label of the x axis. In the second instance, the attribute should describe a list for the ticks of the same axis.

The function effectively returns a `FacetGrid` object.

```py
c = medical_data_visualizer.draw_cat_plot()
print(c)
"""
<seaborn.axisgrid.FacetGrid object at 0x0088E718>
"""
```

Looking at the `axes` object, seaborn highlights two axes objects.

```py
print(c.axes)
"""
[[<matplotlib.axes._subplots.AxesSubplot object at 0x197451A8>
  <matplotlib.axes._subplots.AxesSubplot object at 0x1B743310>]]
"""
```

The axes are however nested two levels deep. In other words, to retrieve the x axis, its labels and ticks, you should write

```py
print(c.axes[0][0])
"""
AxesSubplot(0.0513472,0.116556;0.432133x0.814778)
"""
```

It seems reasonable enough: the catplot creates two bar charts, each with its set of axes.

Sure enough, considering one of the two sets:

```py
print(c.axes[0][0].get_xlabel())
"""
variable
"""

print(c.axes[0][0].get_children())
"""
[<matplotlib.patches.Rectangle object at 0x1B763E98>, <matplotlib.patches.Rectangle object at 0x1B74B280>, ...]
"""
```

The same would be true for `c.axes[0][1]`.

The project is still being developed, so I it is likely that the issue is with the testing suite itself.

### Groupby

I've added `visualizer_update.py` to comply with one step I honestly snubbed when creating the catplot:

> Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.

The script creates a dataframe in a rather convoluted manner, but the goal is to create a data structure similar to the following.

```code
  variable  value  cardio  total
0   active      0       0    106
1   active      0       1    116
2   active      1       0    387
3   active      1       1    391
...
```

Once there is a column already counting the number of the `0`s and `1`s, it is no longer to use a countplot, or `kind=count`, and the script uses the default visualization (`kind=bar`).

It does **not** solve the issue with the testing suite, but highlights several features of the pandas library.

### Docs

The following pages helped a lot:

- [pandas melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html)

- [seaborn catplot](https://seaborn.pydata.org/generated/seaborn.catplot.html)

- [seaborn heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

- [numpy triu](https://numpy.org/doc/stable/reference/generated/numpy.triu.html)

- [matplotlib colorbar](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.colorbar.html)

- [pandas groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)

# Medical Data Visualizer

> Third project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

Just like with the project **demographic-data-analyzer**, there is a `.csv` file describing the data, and this stores a subset of the original source data.

## Assignment

The project asks to create a data visualization to highlight the medical data found in `data.csv`. In details, it asks to go through a series of steps, which I'll describe alongside the necessary code.

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

### Incorrect data

The project asks to filter out the measurement matching the following conditions

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

You repeat the values for each individual column

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
df_long = pd.melt(df_clean, value_vars=[
                  "active", "alco", "cholesterol", "gluc", "overweight", "smoke"])
```

Since the observations need to be differentiated on the basis of the `cardio` property, it is also necessary to consider the matching column; this is achieved with the `id_vars` argument.

```py
pd.melt(df_clean, id_vars="cardio", value_vars=[...])
```

### Bar chart

> create a chart that shows the value counts of the categorical features using seaborn's `catplot()`.

In more details, the data should be split by 'cardio', so that there is one chart for each value (`0` and `1`). Moreover, the bar plot should consider the value counts for the following columns:

- active
- alco
- cholesterol
- gluc
- overweight
- smoke

### Correlation matrix

Plot the correlation matrix using seaborn's `heatmap()`. Mask the upper triangle.

```

```

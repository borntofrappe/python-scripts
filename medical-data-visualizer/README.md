# Medical Data Visualizer

> Third project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

Similarly to the project **demographic-data-analyzer**, there is a `.csv` file describing the data, and this stores a subset of the original source data. Be sure to reference the path toward the file at the top of the script.

Unlike the same project, and the other in the freeCodeCamp series, there is only one solution for this assignment. I have not tackled this project in a previous version.

## Assignment

The project asks to create a data visualization to highlight the medical data found in `data.csv`. In details, it asks to go through the following tasks:

- add an 'overweight' column on the basis of the BMI index. The BMI index can be computed as: `BMI = weight / (height ** 2)`, considering the wright in kilograms, the height in meters. If the index is greater than `25` then the person is overweight. Add a value of `0` for **NOT** overweight and a value `1` for overweight

- normalize the columns to repeat the same convention of `0` being always good, and `1` always bad. For instance, and for the `cholesterol` column, consider a value of `1` as good, and a value greater than `1` as bad. Similarly for the `gluc` column.

- convert the data into long format

- create a chart that shows the value counts of the categorical features using seaborn's `catplot()`. The dataset should be split by 'Cardio' so there is one chart for each 'cardio' value (`0` and `1`)

- clean the data. Filter out the following patient segments, as they represent incorrect data:

  - diastolic pressure is higher then systolic (Keep the correct data with `df['ap_lo'] <= df['ap_hi'])`)
  - height is less than the 2.5th percentile (Keep the correct data with `(df['height'] >= df['height'].quantile(0.025))`)
  - height is more than the 97.5th percentile
  - weight is less then the 2.5th percentile
  - weight is more than the 97.5th percentile

- create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's `heatmap()`. Mask the upper triangle.

## Notes

> due to personal inexperience with the imported libraries, there might be more notes than usual
>
> there is also a `min.py` script where I experiment with the modules on smaller tasks

### overweight column

The height is in centimeters, so be sure to divide the values to have meters instead.

```py
df["overweight"] = df["weight"] / ((df["height"] / 100) ** 2) > 25
```

With this snippet, the column is populated with `False` and `True` booleans, but this can be fixed when normalizing the data.

### normalize data

The idea is to have `0` as good, `1` as bad.

```py
df["overweight"].replace({False: 0, True: 1})
```

This does **NOT** mutate the original data frame. Actually, it doesn't mutate the original column, but returns a new columns with the desired values. To have the dataframe instead:

```py
df_normal = df.replace({False: 0, True: 1})
```

Every boolean is updated. This makes it easier to normalize the `cholesterol` and `gluc` functions as well. Populate the columns with a boolean, and then replace said boolean for every column.

```py
df["cholesterol"] = df["cholesterol"] > 1
df["gluc"] = df["gluc"] > 1

df_normal = df.replace({False: 0, True: 1})
```

### long format

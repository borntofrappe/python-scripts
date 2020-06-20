# [Demographic Data Analyzer](https://repl.it/@borntofrappe/fcc-demographic-data-analyzer)

> Second project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

- there are actually two scripts. One created in the end of January 2020, one in June 2020 as I reviewed the project. The two differ since the project was updated with additional requirements, and since I've learned more about the Python language

## Warning(s)

1. Unlike the other scripts in this repo, running the code in `main.py` will not work. To have the script work as intended, open the `analyzer` script(s) and update the `path` variable so that pandas is able to find the `.csv` file.

   ```py
   path = "ADD-PATH/python-scripts/demographic-data-analyzer/"
   ```

   This is true for both files: `analyzer` and `analyzer-previous`.

2. `analyzer-previous.py` **does not** complete the assignment. It seems my January-self fell short of answering the last question

3. the `.csv` file does not describe the full dataset as provided by the assignment. I made the decision to consider a subset, to just illustrate the point of the scripts.

## Assignment

The goal is to analyze a `.csv` file and answer a series of questions. Questions such as:

- How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels
- What is the average age of men?
- What is the percentage of people who have a Bachelor's degree?
- What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
- What percentage of people without advanced education make more than 50K?
- What is the minimum number of hours a person works per week?
- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
- What country has the highest percentage of people that earn >50K and what is that percentage?
- Identify the most popular occupation for those who earn >50K in India.

## Further Research

I am less than satisfied with the working. Especially when counting the number of times a certain value is repeated in a column, I found the syntax to be rather convoluted.

```py
df[df["education"] == "Bachelors"]["education"].count()
```

Perhaps it's all necessary. `df[df["education"] == "Bachelors"]` returns a dataframe, and using the `count` function immediately would result in a series, not an integer.

A series where each column describe its own count.

```PY
print(df[df["education"] == "Bachelors"].count())

"""
age               86
workclass         86
fnlwgt            86
education         86
...
"""
```

## Update

The dissatisfaction with the solution brought a few modifications, stored in `analyzer_update.py`.

Here's a few lessons learned.

### loc

The `loc` function allows to filter a dataframe according to a condition, and then target a specific column, in one convenient set of square brackets

```py
df[df["sex"] == "Male"]["age"]

df.loc[df["sex"] == "Male", "age"]
```

### Count

I've discovered at least three ways to consider how many times a certain value appears in a column

1. `sum()`

   ```py
   (df["education"] == "Bachelors").sum()
   ```

   `(df["education"] == "Bachelors")` provides a series of booleans, and these are summed together considering `True` equal to `1`, `False` equal to nil, `0`

2. `len()`

   ```py
   len(df[df["education"] == "Bachelors"])
   ```

   In this instance you build a dataframe with only the specific values, and then measure its length

3. `shape`

   ```py
   df[df["education"] == "Bachelors"].shape[0]
   ```

   `shape` provides the dimensions for the filtered data structure, and in its first index it details the number of observations

# Demographic Data Analyzer

> Second project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

- there are actually two scripts. One created in the end of January 2020, one in June 2020 as I reviewed the project. The two differ since the project was updated with additional requirements, and since I've learned more about the Python language

## Warning(s)

1. Running the script might not work, because the `pd.read_csv` function needs to describe the location of the `csv` value.

   Be sure to update the path with the precise folder.

   ```py
   path = "ADD-PATH/python-scripts/demographic-data-analyzer/"
   ```

   This is true for both files: `analyzer` and `analyzer-previous`.

2. `analyzer-previous.py` **does not** complete the assignment. It seems my inexperience with the pandas library stopped me from answering every question.

3. I added a few rows at the bottom of the spreadsheet to ensure that the `native-country` column has value representative of "India". In slicing the dataset, it seems I ended up without a single data point from the country

## Assignment

Starting from a dataset of demographic data (extracted from the 1994 Census database), you must use Pandas to answer a series of questions.

- How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (`race` column)
- What is the average age of men?
- What is the percentage of people who have a Bachelor's degree?
- What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
- What percentage of people without advanced education make more than 50K?
- What is the minimum number of hours a person works per week?
- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
- What country has the highest percentage of people that earn >50K and what is that percentage?
- Identify the most popular occupation for those who earn >50K in India.

## Lessons learned

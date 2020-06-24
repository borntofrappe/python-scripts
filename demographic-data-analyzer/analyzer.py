import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(dir + "/data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # ! return a series
    race_count = df["race"].value_counts()

    # What is the average age of men?
    men = df[df["sex"] == "Male"]
    average_age_men = round(men["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df[df["education"] == "Bachelors"]
    percentage_bachelors = round(
        bachelors["education"].count() / df["education"].count() * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"])]

    lower_education = df[~df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"])]

    # percentage with salary >50K
    higher_education_rich = round(higher_education[higher_education["salary"] == ">50K"]["salary"].count(
    ) / higher_education["salary"].count() * 100, 1)

    lower_education_rich = round(lower_education[lower_education["salary"] == ">50K"]["salary"].count(
    ) / lower_education["salary"].count() * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round(
        min_workers[min_workers["salary"] == ">50K"]["salary"].count() / min_workers["salary"].count() * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    countries = df["native-country"].value_counts()
    rich_countries = df[df["salary"] ==
                        ">50K"]["native-country"].value_counts()
    rich_countries_percentages = (
        rich_countries / countries).fillna(0).sort_values(ascending=False)
    highest_earning_country = rich_countries_percentages.index[0]

    highest_earning_country_percentage = round(
        rich_countries[highest_earning_country] / df[df["native-country"] == highest_earning_country]["native-country"].count() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["salary"] == ">50K") & (
        df["native-country"] == "India")]["occupation"].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

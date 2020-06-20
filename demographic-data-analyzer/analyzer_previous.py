import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('data.csv')
    # How many of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(
        df[df["sex"].isin(["Male"])]["age"].describe()["mean"], 1)

    # What is the percentage of people who have a Bachelors degree?
    bachelors = df["education"][df["education"].isin(["Bachelors"])]
    percentage_bachelors = round(
        bachelors.count() / df["education"].count() * 100, 1)

    # What percentage of the people with AND without `education` equal to `Bachelors`, `Masters`, or `Doctorate` also have a `salary` of `>50K` (Note: Every row of data has salary of either '>50K' or '<=50K')?

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

    # What is the minumum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = int(df["hours-per-week"].describe()["min"])

    # What percentage of the people who work the minumum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round(num_min_workers[num_min_workers["salary"] == ">50K"]["salary"].count(
    ) / num_min_workers["salary"].count() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.

    top_IN_occupation = df[(df["salary"] == ">50K") & (
        df["native-country"].isin(["India"]))]["occupation"].describe()["top"]

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
        print("Top occupations in India:", top_IN_occupation)

    return {'race_count': race_count, 'average_age_men': average_age_men, 'percentage_bachelors': percentage_bachelors, 'higher_education_rich': higher_education_rich, 'lower_education_rich': lower_education_rich, 'min_work_hours': min_work_hours, 'rich_percentage': rich_percentage, 'top_IN_occupation': top_IN_occupation}

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os


def draw_plot():
    # Read data from file
    dir = os.path.dirname(__file__)
    df = pd.read_csv(dir + '/data.csv')

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"],
                s=22, label="Sea level")

    # Create first line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"])

    x1 = int(df.iloc[0]["Year"])
    x2 = 2050
    x = [year + x1 for year in range(x2 - x1)]
    y = [intercept + year * slope for year in x]

    plt.plot(x, y, linewidth=3, linestyle="-", color="red",
             label="Line of best fit " + str(x1) + "-" + str(x2))

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    slope, intercept, rvalue, pvalue, stderr = linregress(
        df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])

    x1 = int(df_2000.iloc[0]["Year"])
    x2 = 2050
    x = [year + x1 for year in range(x2 - x1)]
    y = [intercept + year * slope for year in x]

    plt.plot(x, y, linewidth=3, linestyle="--", color="orange",
             label="Line of best fit " + str(x1) + "-" + str(x2))

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    plt.savefig(dir + '/sea_level_plot.png')
    return plt.gca()

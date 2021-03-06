import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

dir = os.path.dirname(__file__)

df = pd.read_csv(dir + '/data.csv')

plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"],
            s=22, label="Sea level")


slope, intercept, rvalue, pvalue, stderr = linregress(
    df["Year"], df["CSIRO Adjusted Sea Level"])

x1 = int(df.iloc[0]["Year"])
x2 = 2050
y1 = intercept + x1 * slope
y2 = intercept + x2 * slope
plt.plot([x1, x2], [y1, y2], linewidth=3, linestyle="-",
         color="red", label="Line of best fit " + str(x1) + "-" + str(x2))


df_recent = df[df["Year"] >= 2000]
slope, intercept, rvalue, pvalue, stderr = linregress(
    df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

x1 = int(df_recent.iloc[0]["Year"])
x2 = 2050
y1 = intercept + x1 * slope
y2 = intercept + x2 * slope

plt.plot([x1, x2], [y1, y2], linewidth=3, linestyle="--",
         color="orange", label="Line of best fit " + str(x1) + "-" + str(x2))

plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.legend()

plt.savefig(dir + '/sea_level_plot.png')

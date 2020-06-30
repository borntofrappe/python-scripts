import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

dir = os.path.dirname(__file__)

df = pd.read_csv(dir + '/data.csv')


plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")

plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])


slope, intercept, rvalue, pvalue, stderr = linregress(
    df["Year"], df["CSIRO Adjusted Sea Level"])

x0 = df["Year"][0]
x1 = 2050
y0 = intercept + x0 * slope
y1 = intercept + x1 * slope
plt.plot([x0, x1], [y0, y1], linewidth=2,
         color="red", label="Line of best fit")
plt.legend()

plt.savefig(dir + '/sea_level_plot.png')

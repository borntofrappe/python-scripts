import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

dir = os.path.dirname(__file__)

df = pd.read_csv(dir + '/data.csv')


plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
plt.title("Sea Level Rise")
plt.xlabel("Year")
plt.ylabel("Adjusted Sea Level")

plt.savefig(dir + '/sea_level_plot.png')

import matplotlib.pyplot as plt
import pandas as pd
import os

# current directory
dir = os.path.dirname(os.path.realpath(__file__))

# build a data frame from the csv values
# data is accessible by column, using the first row as reference
df = pd.read_csv(dir + "/data.csv")

# figure to produce the static file in plot.png
fig = plt.figure()
plt.title('Google Trends')
plt.xlabel("Time")
plt.ylabel("Interest")
# plot x, y
# label is picked up by plt.legend()
plt.plot(df["day"], df["snake"], label="Snake")
plt.plot(df["day"], df["python"], label="Python")
plt.legend()

fig.savefig(dir + '/plot.png')

import matplotlib.pyplot as plt
import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(dir + "/data.csv", parse_dates=["day"])

fig = plt.figure()

plt.title('Google Trends')
plt.xlabel("Time")
plt.ylabel("Interest")
plt.grid(linewidth=0.5, linestyle="dotted")
plt.plot(df["day"], df["python"], label="Python", c="b")
plt.plot(df["day"], df["snake"], label="Snake", c="r")
plt.legend()

fig.savefig(dir + '/global-interface.png')

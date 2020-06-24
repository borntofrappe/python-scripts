import matplotlib.pyplot as plt
import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(dir + "/data.csv", parse_dates=["day"])

fig, axs = plt.subplots(2, 1)
ax1, ax2 = axs

fig.suptitle("Google Trends")


ax1.plot(df["day"], df["python"], label="Python", c="b")
ax1.set_ylim(bottom=df["snake"].min())
ax1.grid(linewidth=0.5, linestyle="dotted")
ax1.legend()

ax2.plot(df["day"], df["snake"], label="Snake", c="r")
ax2.set_ylim(top=df["python"].max())
ax2.grid(linewidth=0.5, linestyle="dotted")
ax2.legend()

fig.savefig(dir + "/object-oriented-interface.png")

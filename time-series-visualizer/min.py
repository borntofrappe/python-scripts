import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

dir = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(dir + '/' + 'data.csv',
                 index_col="date", parse_dates=["date"])

lower_threshold = df["value"].quantile(0.025)
upper_threshold = df["value"].quantile(0.975)

df_clean = df[(df["value"] > lower_threshold) &
              (df["value"] < upper_threshold)]

fig = plt.figure(figsize=(16, 5))
ax = sns.lineplot(x=df_clean.index, y=df_clean["value"])
ax.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
       xlabel="Date", ylabel="Page Views")

fig.savefig(dir + '/' + './line_plot.png')

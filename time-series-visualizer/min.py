import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

dir = os.path.dirname(os.path.realpath(__file__))

# READ & CLEAN
df = pd.read_csv(dir + '/' + 'data.csv',
                 index_col="date", parse_dates=["date"])

lower_threshold = df["value"].quantile(0.025)
upper_threshold = df["value"].quantile(0.975)

df_clean = df[(df["value"] > lower_threshold) &
              (df["value"] < upper_threshold)]

# LINE CHART
fig_line = plt.figure(figsize=(16, 5))
ax_line = sns.lineplot(x=df_clean.index, y=df_clean["value"])
ax_line.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
            xlabel="Date", ylabel="Page Views")

fig_line.savefig(dir + '/' + './line_plot.png')

# BAR CHART
df_copy = df_clean.copy()
df_group = df_copy.groupby(pd.Grouper(freq="M"))
df_box = df_group.mean()

df_box["month"] = df_box.index.month_name()
df_box["year"] = df_box.index.year

"""
# alternative
df_box = df_box.reset_index()
df_box["month"] = df_box["date"].dt.strftime("%B")
df_box["year"] = df_box["date"].dt.strftime("%Y")
"""

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


fig_bar = plt.figure(figsize=(10, 8))


ax_bar = sns.barplot(x="year", y="value", hue="month",
                     hue_order=months, data=df_box)

ax_bar.set(xlabel="Years", ylabel="Average Page Views")
ax_bar.legend(title="Months", loc="upper left")


fig_bar.savefig(dir + '/' + './bar_plot.png')

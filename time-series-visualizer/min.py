import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

dir = os.path.dirname(__file__)

# READ & CLEAN
print("Reading and cleaning data")
df = pd.read_csv(dir + "/data.csv", parse_dates=["date"], index_col="date")

lower_threshold = df["value"].quantile(0.025)
upper_threshold = df["value"].quantile(0.975)

df = df[(df["value"] > lower_threshold) & (df["value"] < upper_threshold)]

# LINE CHART
print("Creating line chart")
fig_line = plt.figure(figsize=(15, 5))
ax_line = sns.lineplot(x=df.index, y=df["value"])
ax_line.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
            xlabel="Date", ylabel="Page Views")

fig_line.savefig(dir + "/line_plot.png")
print("See **line_plot.png**")

# BAR CHART
print("Prepping data for the bar chart")
df_bar = df.copy()
df_bar = df_bar.groupby(pd.Grouper(freq="M"))
df_bar = df_bar.mean()


df_bar["month"] = df_bar.index.month_name()
df_bar["year"] = df_bar.index.year

"""
# alternative
df_bar = df_bar.reset_index()
df_bar["month"] = df_bar["date"].dt.strftime("%B")
df_bar["year"] = df_bar["date"].dt.strftime("%Y")
"""

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

print("Creating bar chart")
fig_bar = plt.figure(figsize=(10, 8))


ax_bar = sns.barplot(x="year", y="value", hue="month",
                     hue_order=months, data=df_bar)

ax_bar.set(xlabel="Years", ylabel="Average Page Views")
ax_bar.legend(title="Months", loc="upper left")


fig_bar.savefig(dir + "/bar_plot.png")
print("See **bar_plot.png**")


# BOX PLOT
print("Prepping data for the box plot")
df_box = df.copy()
df_box["month"] = df_box.index.month_name()
df_box["year"] = df_box.index.year

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

print("Creating box plot")
fig_box, axs_box = plt.subplots(1, 2, figsize=(17, 5))
ax1, ax2 = axs_box


sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
ax1.set(title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views")

sns.boxplot(x="month", y="value", order=months, data=df_box, ax=ax2)
ax2.set(title="Month-wise Box Plot (Seasonality)", xlabel="Month",
        ylabel="Page Views", xticklabels=[m[:3] for m in months])

fig_box.savefig(dir + "/box_plot.png")
print("See **box_plot.png**")

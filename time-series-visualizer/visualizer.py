import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

dir = os.path.dirname(__file__)

# Import data and clean data
df = pd.read_csv(dir + "/data.csv", parse_dates=["date"], index_col="date")

lower_threshold = df["value"].quantile(0.025)
upper_threshold = df["value"].quantile(0.975)

df = df[(df["value"] > lower_threshold) & (df["value"] < upper_threshold)]


def draw_line_plot():
    # draw line plot
    fig = plt.figure(figsize=(15, 5))
    ax = sns.lineplot(x=df.index, y=df["value"])
    ax.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
           xlabel="Date", ylabel="Page Views")

    fig.savefig(dir + "/line_plot.png")
    return fig


def draw_bar_plot():
    # prep data
    df_bar = df.copy()

    df_bar = df_bar.groupby(pd.Grouper(freq="M")).mean()

    df_bar["month"] = df_bar.index.month_name()
    df_bar["year"] = df_bar.index.year

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # Draw bar plot
    fig = plt.figure(figsize=(10, 8))

    ax = sns.barplot(x="year", y="value", hue="month",
                     hue_order=months, data=df_bar)

    ax.set(xlabel="Years", ylabel="Average Page Views")
    ax.legend(title="Months", loc="upper left")

    fig.savefig(dir + "/bar_plot.png")
    return fig


def draw_box_plot():
    # prep data
    df_box = df.copy()
    df_box["month"] = df_box.index.month_name()
    df_box["year"] = df_box.index.year

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # Draw box plot
    fig, axs = plt.subplots(1, 2, figsize=(17, 5))
    ax1, ax2 = axs

    sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
    ax1.set(title="Year-wise Box Plot (Trend)",
            xlabel="Year", ylabel="Page Views")

    sns.boxplot(x="month", y="value", order=months, data=df_box, ax=ax2)
    ax2.set(title="Month-wise Box Plot (Seasonality)",
            xlabel="Month", ylabel="Page Views", xticklabels=[m[:3] for m in months])

    fig.savefig(dir + "/box_plot.png")
    return fig

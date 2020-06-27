import pandas as pd
import seaborn as sns

import os

print("Reading data from **data.csv**")
dir = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(dir + '/data.csv')

print("Adding overweight column")
df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25)

print("Normalizing data")
df["cholesterol"] = df["cholesterol"] > 1
df["gluc"] = df["gluc"] > 1

df_normal = df.replace({False: 0, True: 1})

print("Creating bar chart")
# catplot
df_long = pd.melt(df_normal, id_vars="cardio", value_vars=[
                  "active", "alco", "cholesterol", "gluc", "overweight", "smoke"])


fig_catplot = sns.catplot(x="variable", hue="value", col="cardio",
                          kind="count", data=df_long)

fig_catplot.savefig(dir + "/catplot.png")
print("Bar chart complete. See **catplot.png**")


"""
# correlation matrix
height_low_percentile = df_normal["height"].quantile(0.025)
height_high_percentile = df_normal["height"].quantile(0.975)

weight_low_percentile = df_normal["weight"].quantile(0.025)
weight_high_percentile = df_normal["weight"].quantile(0.975)

df_clean = df_clean = df_normal[~((df["ap_lo"] > df["ap_hi"]) | (df["height"] < height_low_percentile) | (df["height"] > height_high_percentile) | (
    df["weight"] < weight_low_percentile) | (df["weight"] > weight_high_percentile))]

"""

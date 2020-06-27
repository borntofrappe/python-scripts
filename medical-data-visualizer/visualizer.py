import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

dir = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv(dir + '/data.csv')

# Add 'overweight' column
df['overweight'] = (df["weight"] / ((df["height"] / 100) ** 2) > 25)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = df["cholesterol"] > 1
df["gluc"] = df["gluc"] > 1

df_normal = df.replace({False: 0, True: 1})

# Draw Categorical Plot


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df_normal, value_vars=[
                  "active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = None

    # Draw the catplot with 'sns.catplot()'

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    height_low_percentile = df_normal["height"].quantile(0.025)
    height_high_percentile = df_normal["height"].quantile(0.975)

    weight_low_percentile = df_normal["weight"].quantile(0.025)
    weight_high_percentile = df_normal["weight"].quantile(0.975)
    # Clean the data
    df_heat = df_normal[~((df["ap_lo"] > df["ap_hi"]) | (df["height"] < height_low_percentile) | (df["height"] > height_high_percentile) | (
        df["weight"] < weight_low_percentile) | (df["weight"] > weight_high_percentile))]

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None

    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

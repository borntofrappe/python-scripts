import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

dir = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv(dir + '/data.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'] > 1
df['gluc'] = df['gluc'] > 1

df_normal = df.replace({False: 0, True: 1})

# Draw Categorical Plot


def draw_cat_plot():
    df_cat = pd.melt(df_normal, id_vars='cardio', value_vars=[
        'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    df_group = df_cat.groupby(["variable", "value", "cardio"])
    df_count_series = df_group["value"].count()

    df_count_dataframe = pd.DataFrame(
        df_count_series).rename(columns={"value": "total"})
    df_totals = df_count_dataframe.reset_index()

    fig = sns.catplot(x='variable', y="total", hue='value',
                      col='cardio', data=df_totals)

    fig.savefig(dir + '/catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    height_low_percentile = df_normal['height'].quantile(0.025)
    height_high_percentile = df_normal['height'].quantile(0.975)

    weight_low_percentile = df_normal['weight'].quantile(0.025)
    weight_high_percentile = df_normal['weight'].quantile(0.975)

    df_heat = df_normal[~((df['ap_lo'] > df['ap_hi']) | (df['height'] < height_low_percentile) | (df['height'] > height_high_percentile) | (
        df['weight'] < weight_low_percentile) | (df['weight'] > weight_high_percentile))]

    corr = df_heat.corr()

    mask = np.triu(corr.columns)

    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(data=corr, mask=mask, annot=True,
                fmt='.1f', square=True, cbar_kws={'shrink': 0.5})

    fig.savefig(dir + '/heatmap.png')
    return fig

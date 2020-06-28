import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(dir + '/' + 'data.csv',
                 index_col="date", parse_dates=["date"])

lower_threshold = df["value"].quantile(0.025)
upper_threshold = df["value"].quantile(0.975)
print(lower_threshold)
print(upper_threshold)

df_clean = df[(df["value"] > lower_threshold) &
              (df["value"] < upper_threshold)]
print(len(df))
print(len(df_clean))

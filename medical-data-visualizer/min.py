import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv(dir + '/data.csv')

df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25)

df["cholesterol"] = df["cholesterol"] > 1
df["gluc"] = df["gluc"] > 1

df_normal = df.replace({False: 0, True: 1})

print(df_normal.head())

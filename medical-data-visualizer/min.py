import pandas as pd

path = "ADD-PATH-HERE/python-scripts/medical-data-visualizer/"
df = pd.read_csv(path + 'data.csv')

df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25)

df["cholesterol"] = df["cholesterol"] > 1
df["gluc"] = df["gluc"] > 1

df_normal = df.replace({False: 0, True: 1})

print(df_normal.head())

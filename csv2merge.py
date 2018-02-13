import pandas as pd

a = pd.read_csv("filea.csv")
b = pd.read_csv("fileb.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='title')
merged.to_csv("output.csv", index=False)
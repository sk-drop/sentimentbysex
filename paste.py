import pandas as pd

df = pd.read_csv("./data/new2019final.csv")
df1 = pd.read_csv("./data/new2020final.csv")
df2 = pd.read_csv("./data/new2021final.csv")

df["year"] = 2019
df1["year"] = 2020
df2["year"] = 2021

final = pd.concat([df,df1,df2], axis=0)
final.to_csv("./data/new_relationship_advice_data_19_20_21.csv")
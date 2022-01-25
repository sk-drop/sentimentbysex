import pandas as pd 
import numpy as np


yearlist = [2020]

for x in range(len(yearlist)):

    df = pd.read_csv("./data/new2021v3.csv")
    df = df.dropna()
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.drop(columns=["text" ,'cleanText', 'score', 'title'])
    print(yearlist[x])
    print("n=",len(df))
    df["author_sex"] = df["author_sex"].str.lower()
    df["other_sex"] = df["other_sex"].str.lower()

    df.to_csv("./data/new2021final.csv")


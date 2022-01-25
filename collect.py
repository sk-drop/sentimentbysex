import pandas as pd 
pd.set_option('display.max_rows', None)

df = pd.read_csv("./data/relationship_advice_data_19_20_21.csv")

for index, row in df.iterrows():
    relation = row["other_rel"].lower()
    other = row["other_sex"]
    author = row["author_sex"]
    print(relation)
    if relation in ["gf", "girlfriends"]:
        relation = "girlfriend"
        row["other_rel"] = relation
    if relation in ["bf, boyfriends"]:
        relation = "boyfriend"
        row["other_rel"] = relation

    if relation in ["acquaintance", "coworker", "roommate", "worker"]:
        relation = "distant_friends"
        row["other_rel"] = relation

    if relation in ["bestfriend"]:
        relation = "close_friend"
        row["other_rel"] = relation

    if relation in ["someone"]:
        relation = "random"
        row["other_rel"] = relation

    if relation in ["mom", "mother"]:
        relation = "mother"
        row["other_rel"] = relation

    if relation in ["dad", "father"]:
        relation = "father"
        row["other_rel"] = relation

    if relation in ["bro", "brother"]:
        relation = "brother"
        row["other_rel"] = relation

    if relation in ["sis", "sister"]:
        relation = "sister"
        row["other_rel"] = relation

    if relation in ["daughter"]:
        relation = "daughter"
        row["other_rel"] = relation

    if relation in ["son"]:
        relation = "son"
        row["other_rel"] = relation

    if relation in ["crush"]:
        relation = "crush"
        row["other_rel"] = relation

    if relation in ["he", "guy", "him", "man"]:
        relation = "undefined_male"
        row["other_rel"] = relation

    if relation in ["she", "her", "woman", "lady"]:
        relation = "undefined_female"
        row["other_rel"] = relation

    if relation in ["girl"]:
        relation = "young_undefined_female"
        row["other_rel"] = relation

    if relation in ["boy"]:
        relation = "young_undefined_male"
        row["other_rel"] = relation

    if relation in ["ex", "exboyfriend", "exgirlfriend"]:
        relation = "ex_partner"
        row["other_rel"] = relation

    if other == "f" and relation in ["partner", "fiancé", "SO", "fiance", "fiancée", ] and author == "m":
        relation = "wife"
        row["other_rel"] = relation

    if other == "m" and relation == "partner" and author == "f":
        relation = "husband"
        row["other_rel"] = relation

    else:
        relation = "undefined"
        row["other_rel"] = relation
        print("done")



df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.drop(columns=['id'])
df.to_csv("19ra20ra21ra.csv")
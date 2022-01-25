# importing libraries to be used
import pandas as pd
import re 

# loading data we collected
data = pd.read_csv("./data/new2021.csv")

# TITLE 
# looking for format of title
test = data.loc[12, "title"]
print(test)

# -> Can't wait until Thursday....My(48M) wife(44F) is going to be SHOCKED
# -> My (21F) brother (19M) opened up to me about his penis problems and I don’t know what to do
# -> I (38m) just found out that my brother (19m) has been perving on my wife (37f)

# we want everything in the parenthesis + information about relationship + sentiment

# vars: age/gender author, age/gender involved person(s), type of relationship + t_sentiment

author_identification = ["My", "my", "i", "I", "me", "Me"]
pattern = re.compile(r"(\w+\s*)\((\d+\w)\)")
data["author_age"] = pd.Series()
data["author_sex"] = pd.Series()
data["other_age"] = pd.Series()
data["other_sex"] = pd.Series()
data["other_rel"] = pd.Series()

# extracting relevant data from title
for index, row in data.iterrows():

    matches = re.findall(pattern, row["title"])
    print(matches)

    for match in matches:
        match = list(match)
        match[0] = match[0].strip()
        if match[0] in author_identification:
            demos = re.split(r'(\d+)', match[1])
            data.loc[index, "author_age"] = demos[1]
            data.loc[index, "author_sex"] = demos[2]
        if match[0] not in author_identification and match[0] != 0:
            demos = re.split(r'(\d+)', match[1])
            print(demos)
            data.loc[index, "other_age"] = demos[1]
            data.loc[index, "other_sex"] = demos[2]
            data.loc[index, "other_rel"] = match[0]
        
    
data.to_csv("./data/new2021v2.csv")

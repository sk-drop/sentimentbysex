import praw
from psaw import PushshiftAPI
import pandas as pd
import re
import datetime as dt

r = praw.Reddit(
    client_id="1ZpgI54_RZdyO8lAIK3IJQ",
    client_secret="xtPjxoDxVXZt3o16ewRRtsXpToF6mg",
    user_agent="android:com.example.grabby:v1.2.3 (by u/noscaryghost)")
api = PushshiftAPI(r, detect_local_tz=False)

start_time=int(dt.datetime(2021, 1, 1).timestamp())
end_time=int(dt.datetime(2022, 10, 1).timestamp())

l1 = list(api.search_submissions(after=start_time,
                                before=end_time,
                                subreddit='relationship_advice',
                                filter=['url', 'selftext', 'title'],
                                limit=10000, metadata=True))

df = pd.DataFrame()
df["id"] = []
df["title"] = []
df["text"] = []
df["score"] = []
print(df.head)

# pattern and starting point for index
pattern = re.compile(r"(\(\d+\w\))|(\[\d+[fm]\])")
j = 0

for submission in l1:
    title = submission.title
    matches = ["Update", "UPDATE", "update"]
    crit0 = bool(len(re.findall(pattern, submission.title)) == 2 or len(re.findall(pattern, submission.selftext)) == 2)
    crit1 = bool(any(x in submission.title for x in matches) == 0)
    crit2 = bool(len(submission.selftext) >= 30)
    print(crit0,crit1,crit2)
    if crit0 and crit1 and crit2:
        df.loc[j,"id"] = j
        df.loc[j,"title"] = submission.title
        df.loc[j,"text"] = submission.selftext
        df.loc[j,"score"] = submission.score
        print(df.loc[j,:])
        j+=1

df.to_csv("./data/new2021.csv")

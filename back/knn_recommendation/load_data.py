# load_data.py

import pandas as pd
import json
from surprise import Dataset
from surprise import Reader

# This is the same data that was plotted for similarity earlier
# with one new user "E" who has rated only movie 1

# reads the json file with user data
user_data = [json.loads(line) for line in open('data/user_data.json', 'r')][0]
# print(user_data)

# reads the json file with post data
post_data = [json.loads(line) for line in open('data/post_data.json', 'r')][0]

# Create an 200*1000 table where r[i][j] refers to the 
r = [[0 for j in range(len(post_data)+10)] for i in range(len(user_data)+10)]

print(len(user_data), len(post_data), "llll")

def get_user_data_uid(uid):
    for u in user_data:
        if u['uid'] == uid:
            return u

# prepare the rating table
for u in user_data:
    # print(u)
    uid = u['uid']
    for l in u['liked']:
        r[uid][int(l)] += 0.5
    for c in u['collected']:
        r[uid][int(c)] += 0.7
    for p in u['posted']:
        r[uid][int(p)] += 1
    for following in u['following']:
        # print(following)
        f = get_user_data_uid(int(following))
        if f == None:
            print(f"System Error: Not found user with uid:{following}")
        else:
            for l in f['liked']:
                r[uid][int(l)] += 0.5 * 0.9
            for c in f['collected']:
                r[uid][int(c)] += 0.5 * 0.9
            for p in f['posted']:
                r[uid][int(p)] += 1 * 1.1

maxnum = 0
for u in r:
    for j in u:
        maxnum = max(maxnum, j)

# generate the item, user, rating lists
item, user, rating = [], [], []
for i in range(1, 201):
    for j in range(1, 1001):
        if r[i][j] > 0:
            r[i][j] = float(r[i][j]) / float(maxnum) * 100.0
            item.append(j)
            user.append(i)
            rating.append(r[i][j])

ratings_dict = {
    "item": item,
    "user": user,
    "rating": rating,
}

df = pd.DataFrame(ratings_dict)
reader = Reader(rating_scale = (0, 100))

# Loads Pandas dataframe
data = Dataset.load_from_df(df[["user", "item", "rating"]], reader)
# Loads the builtin Movielens-100k data
# movielens = Dataset.load_builtin('ml-100k')
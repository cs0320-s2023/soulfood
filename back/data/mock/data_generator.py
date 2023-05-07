import json
import random
import numpy as np
import re
from mock.Post import Post
from mock.User import User

# generate 200 users with 1000 posts total
NUM_POST = 1000
NUM_User = 200

# We provide posts with 30 labels
labels = [
    "N/A",
    "Chinese",
    "French",
    "Japanese",
    "Italian",
    "Greek",
    "Spanish",
    "Labanese", 
    "Turkey", 
    "Thai",
    "Indian", 
    "Mexican", 
    "American", 
    # Stories
    "Food therapy",
    "Family made", 
    "Food story", 
    # Environment
    "Great restaurant",
    "Good for brunch", 
    "Good for lunch", 
    "Good for Dinner",
    "Best Ramen Place", 
    "Best for date", 
    "Best for small groups",
    "Best for large groups", 
    "Best for birthday party",
    "Drinks are good",
    "Great music",
    "Clean environment", 
    "Fast serving",
    "Great servers",
    "Line is too long"]

labels_dict = {
    "N/A": 0,
    # Cuisine
    "Chinese": 1,
    "French": 2,
    "Japanese": 3,
    "Italian": 4,
    "Greek": 5,
    "Spanish": 6,
    "Labanese": 7, 
    "Turkey": 8, 
    "Thai": 9,
    "Indian": 10, 
    "Mexican": 11, 
    "American": 12, 
    # Stories
    "Food therapy": 13,
    "Family made": 14, 
    "Food story": 15, 
    # Environment
    "Great restaurant": 16,
    "Good for brunch": 17, 
    "Good for lunch": 18, 
    "Good for Dinner": 19,
    "Best Ramen Place": 20, 
    "Best for date": 21, 
    "Best for small groups": 22,
    "Best for large groups": 23, 
    "Best for birthday party": 24, 
    "Drinks are good": 25,
    "Great music": 26, 
    "Clean environment": 27,
    "Fast serving": 28,
    "Great servers": 29, 
    "Line is too long": 30
}

"""
:param target_list: list to modify and add mocked data to
:param range: range for numbers that can be generated
:param num: secondary range
:return res: final list with random connections between users and posts
"""
def generate_list(target_list, range: tuple, num: tuple):
    x, y = range
    l, h = num
    res = []
    k = []
    index = random.randint(x, y)
    n = random.randint(l,h)
    while(n):
        while(index in k):
            index = random.randint(x, y)
        k.append(index)
        res.append(target_list[index])
        n -= 1
    return res

# prepare the urls
file1 = open('/photo_urls/photo_urls.json', 'r')
urls = file1.read()
urls = json.loads(urls)
print(type(urls[0]))
file1.close()

#prepare the paragraphs
f = open('food.txt', 'r')
data = f.read()
splat = data.split('\n\n')
paragraphs = []
index = 0

# cleans data and returns paragraphs
pg = []
for s in splat:
    if len(s) > 1:
        res = []
        res.append(re.sub('\n', ' ', s))
        if res[0][0] == ' ':
            res[0] = res[0][1:]
        pg.append(res)

print(len(pg))

# cleans data and combines all paragraphs into one list
for i in range(0, NUM_POST + 1):
    n = random.randint(1, 2)
    new_para = []
    while(n):
        n -= 1
        new_para += pg[index]
        index += 1
    paragraphs.append(new_para)


# First, generate 1000 posts with 30 labels. 
uid = 1
posts = []
# used when generating users
liked = [ [] for i in range(NUM_User + 1)]
collected = [ [] for i in range(NUM_User + 1)]
posted = [ [] for i in range(NUM_User + 1)]

while(uid <= NUM_POST):
    # Generate a set of labels
    generated_labels = []
    generated_labels.append(labels[random.randint(1, 12)])
    generated_labels.append(labels[random.randint(13, 15)])
    label_lis = generate_list(labels, (16, 30), (2,5))
    for g in label_lis:
        generated_labels.append(g)
    # User uid list
    uid_list = list(np.arange(0, NUM_User + 1))
    # Generate the list of liked_by
    liked_by = generate_list(uid_list, (1, NUM_User), (5, 50))
    for l in liked_by:
        liked[l].append(uid)
    # Generate the list of collected_by 
    collected_by = generate_list(uid_list, (1, NUM_User), (1, 30))
    for c in collected_by:
        collected[c].append(uid)
    # Generate the new post
    poster = random.randint(1, NUM_User)
    posted[poster].append(uid)

    # Convert the datatypes of liked_by and collected_by
    f_liked_by = []
    f_collected_by = []
    for l in liked_by:
        # if isinstance(l, np.generic):
        #     l = np.asscalar(l)
        l = l.tolist()
        f_liked_by.append(l)
    for c in collected_by:
        c = c.tolist()
        f_collected_by.append(c)

    new_post = Post(uid=uid, posted_by = poster, liked_by = f_liked_by,
                    collected_by = f_collected_by, title = f"Sample Data:{uid}", labels = generated_labels, 
                    paragraph = paragraphs[uid], photo = urls[uid - 1])
    posts.append(new_post)
    uid += 1

# According to the Posts' Users list, generate the Users
uid = 1
users = []
following = [ [] for i in range(NUM_User + 1)]
followed_by = [ [] for i in range(NUM_User + 1)]
while(uid <= NUM_User):
    u = [i for i in range(0, NUM_User + 1)]
    followers = generate_list(u, (1, NUM_User), (1, 50))
    followed_by[uid] = followers
    for f in followers:
        following[f].append(uid)
    uid += 1

for uid in range(0, NUM_User + 1):
    users.append(User(uid = uid, id = "Sample_id", bio = "Sample_bio", following = following[uid], 
                      followed_by = followed_by[uid], liked = liked[uid], collected = collected[uid],
                      posted = posted[uid]))

# Write the json data
file1 = open('user_data.json', 'w')
j_user = []
for u in users:
    j_user.append(u.get_val())
j_user = json.dumps(j_user)
file1.write(j_user)
file1.close()

file2 = open('post_data.json', 'w')
j_post = []
for p in posts:
    j_post.append(p.get_val())
j_post = json.dumps(j_post)
file2.write(j_post)
file2.close()

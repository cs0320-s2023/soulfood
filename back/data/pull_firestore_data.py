import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("data\soulfood-59503-firebase-adminsdk-erydk-5610b1b065.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

posts_ref = db.collection('posts')
docs = posts_ref.stream()

# Convert documents to a dictionary
posts = {}
for doc in docs:
    posts[doc.id] = doc.to_dict()

users_ref = db.collection('profiles')
docs = users_ref.stream()

# Convert documents to a dictionary
users = {}
for doc in docs:
    users[doc.id] = doc.to_dict()

file1 = open('data/user_data.json', 'w')
j_user = json.dumps(users)
file1.write(j_user)
file1.close()

file2 = open('data/post_data.json', 'w')
j_post = json.dumps(posts)
file2.write(j_post)
file2.close()
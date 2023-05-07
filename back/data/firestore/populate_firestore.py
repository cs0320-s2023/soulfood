import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# connect to firebase
cred = credentials.Certificate("data/firestore/soulfood-cf39a-2265a3fc3514.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# reads the json file with user data
user_data = [json.loads(line) for line in open('data/mock/user_data.json', 'r')][0]

# reads the json file with post data
post_data = [json.loads(line) for line in open('data/mock/post_data.json', 'r')][0]

# upload post data to firestore
for p in post_data:
    try:
        doc_ref = db.collection("posts").document(str(p['pid']))
        doc_ref.set(p)
    except Exception as error:
        print("Error uploading JSON data:", error)
print("Post data uploaded successfully")

# upload user data to firestore
for u in user_data:
    try:
        doc_ref = db.collection("profiles").document(str(u['uid']))
        doc_ref.set(u)
    except Exception as error:
        print("Error uploading JSON data:", error)
print("User data uploaded successfully")

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("data/soulfood-2-0-firebase-adminsdk-go325-559e547d27.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# reads the json file with user data
user_data = [json.loads(line) for line in open('data/user_data.json', 'r')][0]

# reads the json file with post data
post_data = [json.loads(line) for line in open('data/post_data.json', 'r')][0]


for p in post_data:
    try:
        doc_ref = db.collection("posts").document(str(p['pid']))
        doc_ref.set(p)
    except Exception as error:
        print("Error uploading JSON data:", error)
print("Post data uploaded successfully")

for u in user_data:
    try:
        doc_ref = db.collection("profiles").document(str(u['uid']))
        doc_ref.set(u)
    except Exception as error:
        print("Error uploading JSON data:", error)
print("User data uploaded successfully")

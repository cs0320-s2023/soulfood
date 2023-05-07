import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

def update_firestore_data(app):

    db = firestore.client(app)

    posts_ref = db.collection('posts')
    docs = posts_ref.stream()

    # print(docs)

    # Convert documents to a dictionary
    posts = []
    for doc in docs:
        posts.append(doc.to_dict())

    users_ref = db.collection('profiles')
    docs = users_ref.stream()
    
    # print(docs)

    # Convert documents to a dictionary
    users = []
    for doc in docs:
        users.append(doc.to_dict())

    with open('data/user_data.json', 'w') as file1:
        j_user = json.dumps(users[0:len(users)-1])
        file1.write(j_user)
        file1.close()

    with open('data/post_data.json', 'w') as file2:
        j_post = json.dumps(posts[0:len(posts)-1])
        file2.write(j_post)
        file2.close()

# update_firestore_data()
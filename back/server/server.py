from flask import Flask, jsonify
from search_post_uid import search_post_by_user
from search_post_key import search_post_by_keyword
from search_post_label import search_post_by_label
from search_user import search_user
from recommend import recommend_posts
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import sys
sys.path.append("data")
import pull_firestore_data

# creates flask app
app = Flask(__name__)

cred = credentials.Certificate("data\soulfood-59503-firebase-adminsdk-erydk-5610b1b065.json")
fireapp = firebase_admin.initialize_app(cred)

# view function to search for posts by a specific user
# endpoint: search/post
@app.route('/search/post/<int:uid>', methods = ['GET'])
def Search_Post_By_User(uid):
    pull_firestore_data.update_firestore_data(fireapp)
    return search_post_by_user(uid)

# view function to search for posts with certain keywords in the paragraphs or titles
# endpoint: search/post
@app.route('/search/post/<string:keyword>', methods = ['GET'])
def Search_Post_By_Keyword(keyword):
    pull_firestore_data.update_firestore_data(fireapp)
    return search_post_by_keyword(keyword)

# @app.route('/search/post/<none>', methods = ['GET'])
# def Search_Post_Empty():
#     return jsonify("Keyword cannot be empty"), 404

# view function to search for posts with a certain label
# endpoint: search/label
@app.route('/search/label/<string:label>', methods = ['GET'])
def Search_Post_By_Label(label):
    pull_firestore_data.update_firestore_data(fireapp)
    return search_post_by_label(label)
    
#  view function to search for a particular user by user id 
# endpoint: search/user
@app.route('/search/user/<int:uid>', methods = ['GET'])
def Search_User(uid):
    pull_firestore_data.update_firestore_data(fireapp)
    return search_user(uid)

# view function to recommend posts
# endpoint: recommend
@app.route('/recommend/<int:uid>/<int:num_recommend>', methods=['GET'])
def Recommend_Posts(uid, num_recommend):
    pull_firestore_data.update_firestore_data(fireapp)
    return recommend_posts(uid, num_recommend)


if __name__ == '__main__':
    pull_firestore_data.update_firestore_data(fireapp)
    app.run(debug=True)
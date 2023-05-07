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
from flask_cors import CORS, cross_origin

# creates flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# creates flask app
app = Flask(__name__)

cred = credentials.Certificate("data/soulfood-2-0-firebase-adminsdk-go325-559e547d27.json")
fireapp = firebase_admin.initialize_app(cred)

# view function to search for posts by a specific user
# endpoint: search/post
@app.route('/search/post/<int:uid>', methods = ['GET'])
@cross_origin()
def Search_Post_By_User(uid):
    # pull_firestore_data.update_firestore_data(fireapp)
    return search_post_by_user(uid)

# view function to search for posts with certain keywords in the paragraphs or titles
# endpoint: search/post
@app.route('/search/post/<string:keyword>', methods = ['GET'])
@cross_origin()
def Search_Post_By_Keyword(keyword):
    # pull_firestore_data.update_firestore_data(fireapp)
    return search_post_by_keyword(keyword)

# when no uid query is provided
@app.route('/search/post/', methods = ['GET'])
@cross_origin()
def Search_Post_By_Key_Empty():
    return jsonify({'error': 'Keyword should not be empty'}), 404

# view function to search for posts with a certain label
# endpoint: search/label
@app.route('/search/label/<string:label>', methods = ['GET'])
@cross_origin()
def Search_Post_By_Label(label):
    # pull_firestore_data.update_firestore_data(fireapp)
    return search_post_by_label(label)

# when label query is not given
@app.route('/search/label/', methods = ['GET'])
@cross_origin()
def Search_Post_By_Label_Empty():
    return jsonify({'error':'Label should not be empty.'}), 404
    
#  view function to search for a particular user by user id 
# endpoint: search/user
@app.route('/search/user/<int:uid>', methods = ['GET'])
@cross_origin()
def Search_User(uid):
    # pull_firestore_data.update_firestore_data(fireapp)
    return search_user(uid)

# when user id query is not given
@app.route('/search/user/', methods = ['GET'])
@cross_origin()
def Search_User_Empty():
    return jsonify({'error': 'User id should not be empty'}), 404

# view function to recommend posts
# endpoint: recommend
@app.route('/recommend/<int:uid>/<int:num_recommend>', methods=['GET'])
@cross_origin()
def Recommend_Posts(uid, num_recommend):
    # pull_firestore_data.update_firestore_data(fireapp)
    return recommend_posts(uid, num_recommend)
# when both uid and num_recommend are not given
@app.route('/recommend/', methods = ['GET'])
@cross_origin()
def Recommend_Posts_Empty():
    return jsonify({'error': 'Recommnedation cannot be given to unspecified user'}), 404
# when num_recommend is not given
@app.route('/recommend/<int:uid>/', methods = ['GET'])
@cross_origin()
def Recommend_Posts_Default(uid):
    return recommend_posts(uid)
            
        


if __name__ == '__main__':
    # pull_firestore_data.update_firestore_data(fireapp)
    app.run(debug=True)
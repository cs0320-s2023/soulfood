import json
from flask import Flask, request, jsonify, json
# from knn_recommendation.recommend_main import get_recommendation
# import sys
# sys.path.append('../knn_recommendation/recommend_main')
import sys
# adding Folder_2 to the system path
sys.path.append("knn_recommendation")
import recommend_main


# reads the json file with user data

user_data = [json.loads(line) for line in open('data/user_data.json', 'r')][0]

# reads the json file with post data
post_data = [json.loads(line) for line in open('data/post_data.json', 'r')][0]

app = Flask(__name__)


# view function to search for posts by a specific user
# endpoint: search_post
@app.route('/search/post/<int:uid>', methods = ['GET'])
def search_post_by_user(uid):
    if request.method == 'GET':
        if uid<0:
            return jsonify('User id should be nonnegative'), 404
        else:
            if len(post_data) > 0:
                searched_posts = []
                for post in post_data:
                    if post['posted_by'] == uid:
                        searched_posts.append(post)
                if searched_posts == []:
                    return jsonify('This user has not posted anything yet.'), 404
                else:
                    return jsonify(searched_posts), 200
            else:
                return jsonify('No post data available'), 404
    else:
        return jsonify('Invalid request'), 500

# view function to search for posts with certain keywords in the paragraphs or titles
# endpoint: search_post
@app.route('/search/post/<string:keyword>', methods = ['GET'])
def search_post_by_keyword(keyword):
    if request.method == 'GET':
        if keyword == ' ':
            return jsonify('Keyword should not be empty'), 404
        else:
            if len(post_data) > 0:
                searched_posts = []
                for post in post_data:
                    if keyword in post['title'] or keyword in post['paragraph'][0]:
                        searched_posts.append(post)
                if searched_posts == []:
                    return jsonify('The keyword is not found in any post.'), 404
                else:
                    return jsonify(searched_posts), 200
            else:
                return jsonify('No post data available'), 404
    else:
        return jsonify('Invalid request'), 500 

# view function to search for posts with a certain label
# endpoint: search_label
@app.route('/search/label/<string:label>', methods = ['GET'])
def search_post_by_label(label):
    if request.method == 'GET':
        if label == '':
            return jsonify('Label should not be empty.'), 404
        else:
            if len(post_data) > 0:
                searched_posts = []
                for post in post_data:
                    if label in post['labels']:
                        searched_posts.append(post)
                if searched_posts == []:
                    return jsonify('No post has been assigned to this label.'), 404
                else:
                    return jsonify(searched_posts), 200
            else:
                return jsonify('No post data available'), 404
    else:
        return jsonify('Invalid request'), 500 
    
#  view function to search for a particular user by user id  
@app.route('/search/user/<int:uid>', methods = ['GET'])
def search_user(uid):
    if request.method == 'GET':
        if uid<0:
            return jsonify('User id should be nonnegative'), 404
        else:
            if len(post_data) > 0:
                searched_user = []
                for user in user_data:
                    if user['uid'] == uid:
                        searched_user = user
                if searched_user == []:
                    return jsonify('This user does not exist.'), 404
                else:
                    return jsonify(searched_user), 200
            else:
                return jsonify('No user data available'), 404
    else:
        return jsonify('Invalid request'), 500

# view function to recommend posts
@app.route('/recommend/<int:uid>/<int:num_recommend>', methods=['GET'])
def recommend_posts(uid, num_recommend):
    if request.method == 'GET':
        if uid<0:
            return jsonify("User id should be nonnegative"), 404
        elif len(user_data) <= 0 :
            return jsonify("No user data available."), 404
        elif len(post_data) <= 0:
            return jsonify("No post data available"), 404
        else:
            this_user = []
            for user in user_data:
                if user['uid'] == uid:
                    this_user = user
            if this_user == []:
                return jsonify("This user does not exist"), 404
            else:
                if num_recommend == None:
                    recommendations = recommend_main.get_recommendation(uid)
                else:
                    recommendations = recommend_main.get_recommendation(uid, num_recommend)
                pids = []
                for recommendation in recommendations:
                    pids.append(recommendation[0])
                posts = []
                for post in post_data:
                    print(posts)
                    if post['pid'] in pids:
                        posts.append(post)
                return jsonify(posts), 200
    else:
        return jsonify('Invalid request'), 500
            
        

if __name__ == '__main__':
    app.run(debug=True)
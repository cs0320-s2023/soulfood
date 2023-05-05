import json
from flask import Flask, request, jsonify, json
# from knn_recommendation.recommend_main import get_recommendation
# import sys
# sys.path.append('../knn_recommendation/recommend_main')
import sys
sys.path.append("knn_recommendation")
import recommend_main


# reads the json file with user data
user_data = [json.loads(line) for line in open('data/user_data.json', 'r')][0]

# reads the json file with post data
post_data = [json.loads(line) for line in open('data/post_data.json', 'r')][0]

# view function to recommend posts
def recommend_posts(uid, num_recommend = 5):
    if request.method == 'GET':
        if uid<0:
            return jsonify({'error': "User id should be nonnegative"}), 404
        elif len(user_data) <= 0 :
            return jsonify({'error': "No user data available."}), 404
        elif len(post_data) <= 0:
            return jsonify({'error': "No post data available"}), 404
        else:
            this_user = []
            for user in user_data:
                if user['uid'] == uid:
                    this_user = user
            # when the searched user id is not a valid user id
            if this_user == []:
                return jsonify({'error': "This user does not exist"}), 404
            else:
                # if num_recommend == None:
                #     recommendations = recommend_main.get_recommendation(uid)
                # else:
                recommendations = recommend_main.get_recommendation(uid, num_recommend)
                # get the ids of recommended posts
                pids = []
                for recommendation in recommendations:
                    pids.append(recommendation[0])
                # get the recommended posts
                posts = []
                for post in post_data:
                    print(posts)
                    if post['pid'] in pids:
                        posts.append(post)
                return jsonify(posts), 200
    else:
        return jsonify({'error': 'Invalid request'}), 500
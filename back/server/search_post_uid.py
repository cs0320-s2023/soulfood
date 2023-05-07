import json
from flask import Flask, request, jsonify, json

# reads the json file with user data
u = open('data/mock/user_data.json', 'r')
user_data = json.load(u)

# reads the json file with post data
p = open('data/mock/post_data.json', 'r')
post_data = json.load(p)

# view function to search for posts by a specific user
def search_post_by_user(uid):
    if request.method == 'GET':
        if uid<0:
            return jsonify({'error': 'User id should be nonnegative'}), 404
        else:
            if len(post_data) > 0:
                searched_posts = []
                for post in post_data:
                    if post['posted_by'] == uid:
                        searched_posts.append(post)
                if searched_posts == []:
                    return jsonify({'error': 'This user has not posted anything yet.'}), 404
                else:
                    return jsonify(searched_posts), 200
            else:
                return jsonify({'error': 'No post data available'}), 404
    else:
        return jsonify({'error': 'Invalid request'}), 500
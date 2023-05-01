import json
from flask import Flask, request, jsonify, json

# reads the json file with user data
user_data = [json.loads(line) for line in open('data/user_data.json', 'r')][0]

# reads the json file with post data
post_data = [json.loads(line) for line in open('data/post_data.json', 'r')][0]

# view function to search for posts by a specific user
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
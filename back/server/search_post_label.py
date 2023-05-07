import json
from flask import Flask, request, jsonify, json

# reads the json file with user data
u = open('data/mock/user_data.json', 'r')
user_data = json.load(u)

# reads the json file with post data
p = open('data/mock/post_data.json', 'r')
post_data = json.load(p)

# view function to search for posts with a certain label
def search_post_by_label(label):
    if request.method == 'GET':
        if label == None:
            return jsonify({'error': 'Label should not be empty.'}), 404
        else:
            if len(post_data) > 0:
                searched_posts = []
                for post in post_data:
                    if label in post['labels']:
                        searched_posts.append(post)
                if searched_posts == []:
                    return jsonify({'error': 'No post has been assigned to this label.'}), 404
                else:
                    return jsonify(searched_posts), 200
            else:
                return jsonify({'error': 'No post data available'}), 404
    else:
        return jsonify({'error': 'Invalid request'}), 500 
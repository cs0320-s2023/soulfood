import json
from flask import Flask, request, jsonify, json

# reads the json file with user data
user_data = [json.loads(line) for line in open('/Users/kelvin/Documents/GitHub/soulfood/back/data/user_data.json', 'r')][0]

# reads the json file with post data
post_data = [json.loads(line) for line in open('/Users/kelvin/Documents/GitHub/soulfood/back/data/user_data.json', 'r')][0]

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
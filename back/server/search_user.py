import json
from flask import Flask, request, jsonify, json

# reads the json file with user data
user_data = [json.loads(line) for line in open('data/user_data.json', 'r')][0]

# reads the json file with post data
post_data = [json.loads(line) for line in open('data/post_data.json', 'r')][0]

#  view function to search for a particular user by user id 
def search_user(uid):
    if request.method == 'GET':
        if uid<0:
            return jsonify({'error': 'User id should be nonnegative'}), 404
        else:
            if len(post_data) > 0:
                searched_user = []
                for user in user_data:
                    if user['uid'] == uid:
                        searched_user = user
                if searched_user == []:
                    return jsonify({'error': 'This user does not exist.'}), 404
                else:
                    return jsonify(searched_user), 200
            else:
                return jsonify({'error': 'No user data available'}), 404
    else:
        return jsonify({'error': 'Invalid request'}), 500
    

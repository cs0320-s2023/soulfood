import json
from flask import Flask, request, jsonify, json

# reads the json file with user data
u = open('data/mock/user_data.json', 'r')
user_data = json.load(u)

# reads the json file with post data
p = open('data/mock/post_data.json', 'r')
post_data = json.load(p)

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
    

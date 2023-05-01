import json
from flask import Flask, request, jsonify, json

# reads the json file with user data

user_data = [json.loads(line) for line in open('data\\user_data.json', 'r')][0]

# reads the json file with post data
post_data = [json.loads(line) for line in open('data\\post_data.json', 'r')][0]

app = Flask(__name__)

# view function to search posts by a specific user
@app.route('/search/<int:uid>', methods = ['GET'])
def search_user(uid):
    if request.method == 'GET':
        if uid<0:
            'Invalid user id', 404
        else:
            if len(post_data) > 0:
                searched_posts = []
                for post in post_data:
                    if post['posted_by'] == uid:
                        searched_posts.append(post)
                return jsonify(searched_posts), 200
            else:
                'Nothing Found', 404
    else:
        'Invalid request', 500

def list_contains(keyword, list):
    for l in list:
        if keyword.lower() in l.lower():
            return True
    return False

# view function to search posts with certain keywords
@app.route('/search/<string:keyword>', methods = ['GET'])
def search_posts(keyword):
    if request.method == 'GET':
        if keyword == '':
            'Keyword should not be empty', 404
        else:
            searched_posts = []
            for post in post_data:
                if keyword.lower() in post['title'].lower() or list_contains(keyword, post['labels']) or list_contains(keyword, post['paragraph']):
                    searched_posts.append(post)
            print(len(searched_posts))
            return jsonify(searched_posts), 200
    else:
        'Invalid request', 500 

if __name__ == '__main__':
    app.run(debug=True)
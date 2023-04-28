import config
import requests
import json

url = "https://api.pexels.com/v1/search?query=food&per_page=80"

NUM_PHOTOS = 1000
photo_urls = []

while len(photo_urls) < NUM_PHOTOS:
    request = requests.get(url, headers={"Authorization":config.pexels_api_key})
    data = request.json()
    print(data)
    for photo in data["photos"]:
        if len(photo_urls) == NUM_PHOTOS:
            break
        photo_urls.append(photo['src']['original'])
    url = data['next_page']

with open("photo_urls.json", "w") as wf:
    json.dump(photo_urls, wf)
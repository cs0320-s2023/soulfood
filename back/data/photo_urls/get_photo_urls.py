import config
import requests
import json

"""
scrapes 1000 images from source site for mocked data usage; single-run script
"""

# scrape site
url = "https://api.pexels.com/v1/search?query=food&per_page=80"

# number of photos to be scraped
NUM_PHOTOS = 1000
photo_urls = []

# loops through data to obtain NUM_PHOTOS urls to photos
while len(photo_urls) < NUM_PHOTOS:
    request = requests.get(url, headers={"Authorization":config.pexels_api_key})
    data = request.json()
    print(data)
    for photo in data["photos"]:
        if len(photo_urls) == NUM_PHOTOS:
            break
        photo_urls.append(photo['src']['original'])
    url = data['next_page']

# urls are stored in photo_urls.json
with open("photo_urls.json", "w") as wf:
    json.dump(photo_urls, wf)
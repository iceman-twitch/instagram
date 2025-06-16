import requests
from bs4 import BeautifulSoup
import json


def get_instagram_userid(username):

    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # a = str(soup)
    # with open("soup.txt", "+w") as f:
        # f.write(a)
    # Extract the window._sharedData object
    script_tag = soup.find('script', {'type': 'application/json'})
    shared_data = json.loads(script_tag.text)

    # Extract the owner object
    owner = shared_data['entry_data']['ProfilePage'][0]['graphql']['user']

    # Get the user ID
    userid = owner['id']

    return userid


username = "iceman__twitch"  # Replace with the Instagram username you want to get the ID for
userid = get_instagram_userid(username)
print(f"User ID: {userid}")
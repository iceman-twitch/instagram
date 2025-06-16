import requests
import json

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

}

import json


url = "https://www.instagram.com/{username}/?__a=1"

def find_instagram_profile(user_id, session_id):
    url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
    headers = {
        'User-Agent': 'Instagram 10.3.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+',
        'Cookie': f'sessionid={session_id}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        username = user_info['user']['username']
        return f"https://www.instagram.com/{username}/"
    else:
        return "Unable to retrieve profile."

def find_instagram_id_by_username():
    url = "https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    if response.status_code == 200:
        profilePage_
        user_id_start = response.text.find('"profilePage_', 0) + len('"profilePage_')
        user_id_end = response.text.find('"', user_id_start)
        user_id = response.text[user_id_start:user_id_end]
        print( user_id )
        return user_id
    else:
        print('0')
        return None
        



import os
import re
import random
import string
import requests
from datetime import datetime

def extractCsrftoken(s):
    s.headers.update({
        'authority':'www.instagram.com',
        'method':'GET',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    })
    response = s.get("https://www.instagram.com/")
    pattern = r'"csrf_token":"(.*?)"'
    match = re.search(pattern, response.text)
    # print(response.text)
    csrftoken = ''
    if match:
        csrftoken = match.group(1)
        print(csrftoken)
    else:
        print("CSRF token not found")
    return csrftoken

def checkUsernameAvailability(session, username):
    requestUrl = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
    session.headers.update({
        'authority':'www.instagram.com',
        'method':'POST',
        'path':'/api/v1/web/accounts/web_create_ajax/attempt/',
        'scheme':'https',
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br, zstd',
        'Accept-Language':'fr',
        'Content-Type':'application/x-www-form-urlencoded',
        'Origin':'https://www.instagram.com',
        'Priority':'u=1, i',
        'Referer':'https://www.instagram.com/accounts/emailsignup/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Csrftoken': csrftoken,
        'X-Requested-With':'XMLHttpRequest'
    })
    randomEmail = ''.join(random.choices(string.ascii_lowercase, k=15)) + '@gmail.com'
    randomPassword = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=16))
    randomFirstName = ''.join(random.choices(string.ascii_lowercase, k=8)) + ' ' + ''.join(random.choices(string.ascii_lowercase, k=5))
    requestPayload = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(datetime.now().timestamp()), randomPassword),
        'email': randomEmail,
        'first_name': randomFirstName,
        'username': username,
        'opt_into_one_tap': 'false'
    }
    response = session.post(requestUrl, data=requestPayload)
    return response.json()
    
def get_userinfo(s,userid):
    url = "https://i.instagram.com/api/v1/users/{user_id}/info/"
    response = s.get(url)
    if response.status_code == 200:
        data = response.text
        # print(data)
        return data
    else:
        print("Not Found")
        return None
def get_userid(s,csrftoken):
    url = "https://www.instagram.com/{username}/?__a=1"
    s.headers.update({
        'method':'GET',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Csrftoken': csrftoken,
    })
    response = s.get(url)
    if response.status_code == 200:
        print(response.text)
        user_id_start = response.text.find('"profilePage_', 0) + len('"profilePage_')
        user_id_end = response.text.find('"', user_id_start)
        user_id = response.text[user_id_start:user_id_end]
        print( user_id )
        
        return user_id
    else:
        print('0')
        return None
    
    
session = requests.session()
csrftoken = extractCsrftoken(session)
# b = get_userid(session,csrftoken)
# c = get_userinfo(session,b)
# username = ''
# while username != '-1':
    # username = str(input("Username: "))
    # data = checkUsernameAvailability(session, username)
    # if 'errors' in data.keys():
        # print(data['errors']['username'][-1]['code'].replace('_', ' '))
        # continue
    # else:
        # print('Username is not taken.')
### WORKS PERFECTLY

# Make a GET request to the Instagram homepage




# Extract the CSRF token from the HTML response



# if match:

    # csrftoken = match.group(1)

    # print(csrftoken)

# else:

from bs4 import BeautifulSoup


username = "central_bigmac"  # Replace with the desired username


url = f"https://www.instagram.com/{username}/"

response = requests.get(url)
print( response.text )

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    script_tag = soup.find('script', {'type': 'application/json'})

    json_data = json.loads(script_tag.text)

    user_id = json_data['csrftoken']

    print(f"User ID: {user_id}")

else:

    print("Failed to retrieve user ID")
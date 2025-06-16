import requests
import instaloader
import json
from bs4 import BeautifulSoup
from functools import partial
from datetime import datetime, timedelta
import time
import random
# s = requests.Session()
# username = "central_bigmac"
# ig = instaloader.Instaloader()
# profile = instaloader.Profile.from_username(ig.context, username)
# user_id = profile.userid
# print(f"User ID: {user_id}")
# profile_pic_url = profile.profile_pic_url
# print(f"Profile Picture URL: {profile_pic_url}")


passwd = "ValamiKurva2004"

user_agent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ' '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
header = {'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Host': 'www.instagram.com',
    'Origin': 'https://www.instagram.com',
    'Referer': 'https://www.instagram.com/',
    'User-Agent': user_agent,
    'X-Instagram-AJAX': '1',
    'X-Requested-With': 'XMLHttpRequest'}
del header['Host']
del header['Origin']
del header['X-Instagram-AJAX']
del header['X-Requested-With']


session = requests.Session()
session.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1',
    'ig_vw': '1920', 'ig_cb': '1', 'csrftoken': '',
    's_network': '', 'ds_user_id': ''})
session.headers.update(header)
# Override default timeout behavior.
# Need to silence mypy bug for this. See: https://github.com/python/mypy/issues/2427
session.request = session.request # type: ignore

# Make a request to Instagram's root URL, which will set the session's csrftoken cookie
# Not using self.get_json() here, because we need to access the cookie
session.get('https://www.instagram.com/')
# Add session's csrftoken cookie to session headers
csrf_token = session.cookies.get_dict()['csrftoken']
session.headers.update({'X-CSRFToken': csrf_token})
print(csrf_token)
enc_password = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(datetime.now().timestamp()), passwd)
time.sleep(min(random.expovariate(0.6), 15.0))
print(enc_password)
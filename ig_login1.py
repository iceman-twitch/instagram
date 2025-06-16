import requests
import json
from datetime import datetime, timedelta
import time
import random

class teveclub():
    def __init__(self, usr, psw):
        self.session = requests.Session()
        self.usr = usr
        self.psw = psw
        self.session_id = ""
        self.enc_password = ""
        self.index_url = "https://www.instagram.com/"
        self.login_url = "https://www.instagram.com/accounts/login/ajax/"

    def enc_password(self):
        self.enc_password = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(datetime.now().timestamp()), self.psw)

    def default_header(self):
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
        if len(self.session_id) == 0:
            del header['Host']
            del header['Origin']
            del header['X-Instagram-AJAX']
            del header['X-Requested-With']

    def get_csrf_token(self):
        self.csrf_token = self.session.cookies.get_dict()['csrftoken']
        print(self.csrf_token)
        self.session.headers.update({'X-CSRFToken': self.csrf_token})

    def get_sessionid(self,response):
        self.session_id = response.cookies.get("sessionid")

    def login(self):
        response = self.session.post(self.login_url, data={'enc_password': self.enc_password, 'username': username}, allow_redirects=True)
        # Check if the login was successful
        if response.status_code == 200:
            json_response = response.json()
            if json_response["authenticated"]:
                self.get_sessionid(response)
                print(f"Login successful! Session ID: {self.session_id}")
                print(self.session_id)
                return
            else:
                print("Login failed. Check your credentials.")
                return
        else:
            print("Login failed. Check your credentials.")
            return
        
def instagram_login(username, password):
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
    # Step 1: Get the CSRF token

    session = requests.Session()
    session.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1',
        'ig_vw': '1920', 'ig_cb': '1', 'csrftoken': '',
        's_network': '', 'ds_user_id': ''})
    session.headers.update(header)
    session.request = session.request # type: ignore

    # Make a request to Instagram's root URL, which will set the session's csrftoken cookie
    # Not using self.get_json() here, because we need to access the cookie
    session.get('https://www.instagram.com/')
    # Add session's csrftoken cookie to session headers
    csrf_token = session.cookies.get_dict()['csrftoken']
    print(csrf_token)
    session.headers.update({'X-CSRFToken': csrf_token})

    # Step 2: Send the login request
    url = "https://www.instagram.com/accounts/login/ajax/"
    
    enc_password = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(datetime.now().timestamp()), password)
    response = session.post(url, data={'enc_password': enc_password, 'username': username}, allow_redirects=True)

    # Check if the login was successful
    if response.status_code == 200:
        json_response = response.json()
        if json_response["authenticated"]:
            session_id = response.cookies.get("sessionid")
            print(f"Login successful! Session ID: {session_id}")
            print(session_id)
            return session_id
        else:
            print("Login failed. Check your credentials.")
            return None
    else:
        print("Login failed. Check your credentials.")
        return None


username = "your_username"  # Replace with your Instagram username
password = "your_password"  # Replace with your Instagram password
# session_id = instagram_login(username, password)
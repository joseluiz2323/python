from asyncio import sleep
import json
from datetime import datetime
from typing import BinaryIO
from bs4 import BeautifulSoup
import requests
import os
import time
from typing import BinaryIO
import requests
import json
import asyncio


class Trenstagram:
    def __init__(self):
        self.BASE_URL = 'https://www.instagram.com/'
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        self.session = requests.Session()
        self.session.headers = {'user-agent': self.USER_AGENT}
        self.session.headers.update({'Referer': self.BASE_URL})
        self.logged_in = False

    def new_login(self, USERNAME, PASSWD):
        self.PASSWD = PASSWD
        self.username = USERNAME
        try:
            req = self.session.get(self.BASE_URL)
            self.session.headers.update(
                {'X-CSRFToken': req.cookies['csrftoken']})
            str_time = str(int(time.time()))
            PASSWORD = '#PWD_INSTAGRAM_BROWSER:0:' + str_time + ':' + PASSWD
            login_data = {'username': USERNAME, 'enc_password': PASSWORD}
            LOGIN_URL = self.BASE_URL + 'accounts/login/ajax/'
            login = self.session.post(
                LOGIN_URL, data=login_data, allow_redirects=True)
            self.session.headers.update(
                {'X-CSRFToken': login.cookies['csrftoken']})
            self.csrftoken = login.cookies['csrftoken']
            self.session_id = self.session.cookies['sessionid']
           # pegar o cookie
            self.cookie = login.headers['set-cookie']
            if(login.json()['authenticated']):
                self.logged_in = True
                print("Logged successfully")
                return True
            else:
                raise Exception()
        except:
            print("Erro ao logar")
        return False

    def verify(self):
        if self.logged_in:
            try:
                r2 = self.session.get(self.BASE_URL + "accounts/edit/")
                # extrair country_code
                self.email = r2.text.split('"email":')[1].split(',')[
                    0].replace('"', '')
            except:
                try:
                    r2 = self.session.get(self.BASE_URL + "accounts/edit/")
                # extrair country_code
                    self.email = r2.text.split('"email":')[1].split(',')[
                        0].replace('"', '')
                except:
                    Trenstagram.new_login(self, self.username, self.PASSWD)
                    print('Error Getting Email')
            return True
        print("Faça login primeiro")
        return False

    def new_username(self, new_username):
        if self.verify():
            try:
                data = {
                    'username': new_username,
                    'email': self.email
                }
                r = self.session.post(
                    self.BASE_URL + "accounts/edit/", data=data)
                if r.json()['status'] == "ok":
                    print(f'Username Changed to {new_username}')
                    self.username = new_username
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Username')
        return False

    def new_bio(self, new_bio):
        if self.verify():
            try:
                data = {
                    'username': self.username,
                    'biography': new_bio,
                    'email': self.email
                }
                r = self.session.post(
                    self.BASE_URL + "accounts/edit/", data=data)
                if r.json()['status'] == "ok":
                    print(f'Bio Changed to {new_bio}')
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Bio')
        return False

    def new_name(self, new_name):
        if self.verify():
            try:
                data = {
                    'username': self.username,
                    'first_name': new_name,
                    'email': self.email
                }
                r = self.session.post(
                    self.BASE_URL + "accounts/edit/", data=data)
                if r.json()['status'] == "ok":
                    print(f'Name Changed to {new_name}')
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Name')
        return False

    def new_website(self, new_website):
        if self.verify():
            try:
                data = {
                    'username': self.username,
                    'external_url': new_website,
                    'email': self.email
                }
                r = self.session.post(
                    self.BASE_URL + "accounts/edit/", data=data)
                if r.json()['status'] == "ok":
                    print(f'Website Changed to {new_website}')
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Website')
        return False

    def new_foto_perfil(self, image_url):
        if self.verify():
            with open(image_url, 'rb') as image:
                photo = image.read()
            try:
                data = {"Content-Disposition": "form-data", "name": "profile_pic",
                        "filename": "profilepic.jpg", "Content-Type": "image/jpeg"}
                #image_req = requests.get(image_url).content
                pfp = bytes(photo)
                self.session.headers.update({'Content-Length': str(len(pfp))})
                r = self.session.post(
                    self.BASE_URL + "accounts/web_change_profile_picture/", files={'profile_pic': pfp}, data=data)
                if r.json()['changed_profile']:
                    print("Profile picture changed!")
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Profile Image')
        return False

    def Save_login(self):
        with open('cookies.txt', 'w+') as f:
            json.dump(self.session.cookies.get_dict(), f)
        with open('headers.txt', 'w+') as f:
            json.dump(self.session.headers, f)

    def AddCH(self):
        try:
            with open('cookies.txt', 'r') as f:
                self.session.cookies.update(json.load(f))
            with open('headers.txt', 'r') as f:
                self.session.headers = json.load(f)
        except:
            return False

    def mudar_genero(self, string):
        CHANGE_URL = "https://www.instagram.com/accounts/set_gender/"
        if string == "M":
            gender = 1
        else:
            gender = 2

        CHANGE_DATA = {"gender": gender, 'custom_gender': ''}

        r = self.session.post(CHANGE_URL, data=CHANGE_DATA)

    def upload_photo(self, photo: BinaryIO):
        micro_time = int(datetime.now().timestamp())

        headers = {
            "content-type": "image / jpg",
            "content-length": "1",
            "X-Entity-Name": f"fb_uploader_{micro_time}",
            "Offset": "0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
            "x-entity-length": "1",
            "X-Instagram-Rupload-Params": f'{{"media_type": 1, "upload_id": {micro_time}, "upload_media_height": 1080,'
                                          f' "upload_media_width": 1080}}',
            "x-csrftoken": self.csrftoken,
            "x-ig-app-id": "1217981644879628",
        }
        cookies = {
            "sessionid": self.session_id,
            "csrftoken": self.csrftoken
        }

        upload_response = requests.post(f'https://www.instagram.com/rupload_igphoto/fb_uploader_{micro_time}',
                                        data=photo, headers=headers, cookies=cookies)

        json_data = json.loads(upload_response.text)
        upload_id = json_data['upload_id']

        if json_data["status"] == "ok":
            return upload_id

        raise Exception(json_data)

    def post(self, photo: BinaryIO, caption=""):

        upload_id = Trenstagram.upload_photo(self, photo)

        url = "https://www.instagram.com/create/configure/"

        payload = f'upload_id={upload_id}&caption={caption}&usertags=&custom_accessibility_caption=&retry_timeout='
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR2-43UfYbG2ZZLxh-BQ8N0rqGa-hESkcmxat2RqMAXejXE3',
            'x-instagram-ajax': 'adb961e446b7-hot',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': '1217981644879628',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/create/details/',
            'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
        }

        cookies = {
            "sessionid":  self.session_id,
            "csrftoken": self.csrftoken
        }

        response = requests.request(
            "POST", url, headers=headers, data=payload, cookies=cookies)
        try:

            json_data = json.loads(response.text)
        except:
            print(response.text)
            return False
        if json_data["status"] == "ok":
            return json_data

        raise Exception(json_data)

    def story(self, photo, caption=""):

        upload_id = Trenstagram.upload_photo(self, photo)

        url = "https://www.instagram.com/create/configure_to_story/"

        payload = f'upload_id={upload_id}&caption={caption}'
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR3ZEXbtmat2-n-xCNYMcmuUO3wQxV_TwIkcccquQjq_2h-O',
            'x-instagram-ajax': '894dd5337020',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': '1217981644879628',
            'origin': 'https://www.instagram.com',
            "sec-ch-ua-platform": "Android",
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/create/story/',
            'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
        }

        cookies = {
            "sessionid":  self.session_id,
            "csrftoken": self.csrftoken
        }

        story_response = requests.request(
            "POST", url, headers=headers, data=payload, cookies=cookies)
        json_data = json.loads(story_response.text)

        if json_data["status"] == "ok":
            response = {
                "message": 'story was shared successfully!',
                'data': json_data}

            return response

        raise Exception(json_data)

    def remover_block(self):

        self.session.headers.update(
            {
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": "https://www.instagram.com/challenge/?next=/",
                'x-instagram-ajax': '894dd5337020',
                "X-Requested-With": "XMLHttpRequest",
                "X-ASBD-ID": "198387",
                "X-IG-App-ID": "936619743392459",
                "X-IG-WWW-Claim": "hmac.AR2QUhgG0rWmfyYVK_PuxTT0fB41fGGM4xPQfTg04UpHRoP8"})
        r = self.session.get('https://www.instagram.com/challenge/',
                             headers=self.session.headers, cookies=self.session.cookies)
        r


log = Trenstagram()
log.AddCH()
log.new_login('blendahunt8', 'gen1122')
log.Save_login()
# with open("imgs\\post.jpg", "rb") as f:
#     log.post(f, "teste")
# sleep(10)
log.remover_block()


from base import Base
import html

import unittest,requests, json,sys,os,time
from requests_toolbelt import MultipartEncoder
import urllib3
urllib3.disable_warnings()

import string,random,pymysql
from datetime import datetime
from colorama import *

stamp = datetime.now().strftime("%Y-%m-%d%  %H:%m:%S %p")   #2017-11-14 07:00:00
stampdate = datetime.now().strftime("%Y-%m-%d% ")
stamptime = datetime.now().strftime("% %H:%m:%S %p")
emailstamp = datetime.now().strftime("%Y%m%d%H%M%S")
email="api_user_" + emailstamp + "@gmail.com"
email1= "api_user_" + emailstamp + "@cmail.com"
email2= "api_user_" + emailstamp + "@amail.com"
email3= "api_user_" + emailstamp + "@bmail.com"
user="api_user_" + emailstamp

def __init__(self):
    at_c = Base.test_accessTokenClient(self)
    at_t = Base.test_accessTokenTrainer(self)
#
#
# h1 = {"Authorization":"Bearer " +"cf5df12312e2a03b68baf269ba145489"}
#
#
# print(h1)
#
#
# p = {"id": 1}
# # headers2 = {'Content-Type': 'application/json',
# #             'Authorization': 'Bearer {}'.format(at_t)}
#
# url = 'https://api-stage.handstandapp.com/api/v3/quiz'
for i in range(1, 4):
    p1 = i
# #     # print(Fore.BLUE + str(p1))
# # print(headers1)
# r = requests.post(url, p, h1,verify=False)
# print(r.)
#
# if r.status_code != 200:
#     print(Fore.RED + r.headers["content-type"])
#     print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(
#         r.status_code))
#     print(Fore.RED + r.content.decode("utf-8"))
#
# elif r.headers["content-type"] != 'application/json':
#     print(
#         Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers[
#             'content-type'])
# else:
#     print("[SUCCESS]when calling[" + url + "]")
#     info = r.content
#     print(info)
#     print(json.dumps(r.json(), indent=4))
#     time.sleep(5)

    url = "https://api-stage.handstandapp.com/api/v3/quiz"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n"+str(p1)+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'authorization': "Bearer 6a46251f4cf016d6a5ebad4dd72fdb46",
    }

    response = requests.request("POST", url, data=payload, headers=headers,verify=False)

    print(response.text)
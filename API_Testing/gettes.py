import requests, json,sys,os
from requests_toolbelt import MultipartEncoder

import unittest,os,time,sys,json
import requests.packages.urllib3
import string,random,pymysql
from datetime import datetime
from colorama import *
requests.packages.urllib3.disable_warnings()
stamp = datetime.now().strftime("%Y-%m-%d%  %H:%m:%S %p")   #2017-11-14 07:00:00
stampdate = datetime.now().strftime("%Y-%m-%d% ")
stamptime = datetime.now().strftime("% %H:%m:%S %p")
emailstamp = datetime.now().strftime("%Y%m%d%H%M%S")
email="api_user_" + emailstamp + "@gmail.com"
time.sleep(5)
r1 = requests.get(
    'https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=11111111')
data = r1.content
d = json.loads(data.decode('utf-8'))

get_urls = ['https://stage.handstandapp.com/api/login?email=&password=11111111',
            'https://stage.handstandapp.com/api/login?email=handstand&password=11111111',
            'https://stage.handstandapp.com/api/login?email=handstand%40gmail.com&password=11111111',
            'https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=',
            'https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=44',
            ]
host_address = 'https://stage.handstandapp.com'
for rest_url in get_urls:
    r = requests.get(rest_url)
    time.sleep(4)
    try:
        if r.status_code != 200:
            a = r.json()

            if ", ".join(a['errors']) == 'The email field is required.':
                assert str(r.status_code) == 422
                assert r.headers["content-type"] == 'application/json'
                assert a['result'] == 'error'
                assert ", ".join(a['errors']) == 'The email field is required.'
                print(Fore.GREEN + "[PASS]when calling[" + rest_url + "]", a)


            elif ", ".join(a['errors']) == 'The email must be a valid email address.':
                assert r.status_code == 422
                assert r.headers["content-type"] == 'application/json'
                assert a['result'] == 'error'
                assert ", ".join(a['errors']) == 'The email must be a valid email address.'
                print(Fore.GREEN + "[PASS]when calling[" + rest_url + "]", a)

            elif ", ".join(a['errors']) == 'Email or password was incorrect.':
                assert r.status_code == 403
                assert r.headers["content-type"] == 'application/json'
                assert a['result'] == 'error'
                assert ", ".join(a['errors']) == 'Email or password was incorrect.'
                print(Fore.GREEN + "[PASS]when calling[" + rest_url + "]", a)
            elif ", ".join(a['errors']) == 'The password field is required.':
                assert r.status_code == 422
                assert r.headers["content-type"] == 'application/json'
                assert a['result'] == 'error'
                assert ", ".join(a['errors']) == 'The password field is required.'
                print(Fore.GREEN + "[PASS]when calling[" + rest_url + "]", a)
            elif ", ".join(a['errors']) == 'Email or password was incorrect.':
                assert r.status_code == 403
                assert r.headers["content-type"] == 'application/json'
                assert a['result'] == 'error'
                assert ", ".join(a['errors']) == 'Email or password was incorrect.'
                print(Fore.GREEN + "[PASS]when calling[" + rest_url + "]", a)
            else:
                print("[FAIL]when calling[" + rest_url + "]", ", ".join(a['errors']))
        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + rest_url + "] got back non JSON data:" + r.headers[
                'content-type'])
        else:
            print('\n')
            print(
                '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('\n')
            print(Fore.RED + "[FAIL]when calling[" + rest_url + "]")
    except:
        pass

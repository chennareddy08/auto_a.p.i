import unittest
from colorama import *
import requests, json,sys,os,time
from requests_toolbelt import MultipartEncoder
import urllib3
urllib3.disable_warnings()

class Base(unittest.TestCase):



    @classmethod
    def setUp(cls):
        pass



    def test_accessTokenClient(self):
        url = 'https://api-stage.handstandapp.com/api/v3/login'
        p1 = {'email': 'APItest@gmail.com', 'password': 11111111}

        r = requests.post(url, p1, verify=False)
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))

        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            data = r.content
            d = json.loads(data.decode('utf-8'))
            at_client = d['access_token']
            return at_client

            #print(at_client)
            time.sleep(5)








    def test_accessTokenTrainer(self):
        url = 'https://api-stage.handstandapp.com/api/v3/trainerlogin'
        p1 = {'email': 'webauto@handstandapp.com', 'password':'handstand'}

        r = requests.post(url, p1, verify=False)
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))

        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            data = r.content
            d = json.loads(data.decode('utf-8'))
            at_trainer = d['access_token']
            return at_trainer
            #print(at)
            time.sleep(5)





    @classmethod
    def tearDown(cls):
        pass





if __name__ == "__main__":
    unittest.main()







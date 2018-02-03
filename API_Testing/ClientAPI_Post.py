
from base import Base
import unittest,requests,json,sys,os,time
from requests_toolbelt import MultipartEncoder
import urllib3
urllib3.disable_warnings()
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
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
time.sleep(5)
time.sleep(5)





class HandstandAPI(Base):


    # def test_loginClientAPI(self):
    #     url = 'https://api-stage.handstandapp.com/api/v3/login'
    #
    #     p1 = {'email': 'APItest@gmail.com', 'password': 11111111, }
    #     p2 = {'password': 11111111, }
    #     p3 = {'email': 'APItest@gmail.com'}
    #     p4 = {'email': 'random@gmail.com', 'password': '11111111', }
    #     p5 = {'email': 'APItest@gmail.com', 'password': 'random', }
    #
    #     s = p1, p2, p3, p4, p5
    #     for i in s:
    #         r = requests.post(url, i, verify=False)
    #         if r.status_code != 200:
    #             print(Fore.RED + r.headers["content-type"])
    #             print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
    #             print(Fore.RED + json.dumps(r.json(), indent=4))
    #
    #         elif r.headers["content-type"] != 'application/json':
    #             print(
    #                 Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
    #         else:
    #             print("[SUCCESS]when calling[" + url + "]")
    #             info = r.content
    #             print(info)
    #             data = r.content
    #             d = json.loads(data.decode('utf-8'))
    #             at = d['access_token']
    #             print(at)
    #
    #             print(json.dumps(r.json(), indent=4))
    #             time.sleep(5)
    #
    # def test_loginTrainerAPI(self):
    #
    #     url = 'https://api-stage.handstandapp.com/api/v3/trainerlogin'
    #     p1 = {'email': 'webauto@handstandapp.com', 'password': 'handstand'}
    #     p2 = {'password': 'handstand', }
    #     p3 = {'email': 'webauto@handstandapp.com'}
    #     p4 = {'email': 'random@gmail.com', 'password': 'handstand', }
    #     p5 = {'email': 'webauto@handstandapp.com', 'password': 'random', }
    #
    #     s = p1, p2, p3, p4, p5
    #     for i in s:
    #         r = requests.post(url, i, verify=False)
    #         if r.status_code != 200:
    #             print(Fore.RED + r.headers["content-type"])
    #             print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
    #             print(Fore.RED + json.dumps(r.json(), indent=4))
    #
    #         elif r.headers["content-type"] != 'application/json':
    #             print(
    #                 Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
    #         else:
    #             print("[SUCCESS]when calling[" + url + "]")
    #             info = r.content
    #             print(info)
    #             data = r.content
    #             d = json.loads(data.decode('utf-8'))
    #             at = d['access_token']
    #             print(at)
    #
    #             print(json.dumps(r.json(), indent=4))
    #             time.sleep(5)

    #
    # def test_signupClientAPI(self):
    #
    #     url = 'https://api-stage.handstandapp.com/api/v3/register'
    #     p1 = {"password": "handstand", "first_name": user, "last_name": user, "mobile": 4244420933, "reebok_accept": 0}
    #     p2 = {"email": email, "first_name": user, "last_name": user, "mobile": 4244420933, "reebok_accept": 0}
    #     p3 = {"email": email, "password": "handstand", "last_name": user, "mobile": 4244420933, "reebok_accept": 0}
    #     p4 = {"email": email, "password": "handstand", "first_name": user, "mobile": 4244420933, "reebok_accept": 0}
    #     p5 = {"email": email, "password": "handstand", "first_name": user, "last_name": user, "reebok_accept": 0}
    #     p6 = {"email": email, "password": "handstand", "first_name": user, "last_name": user, "mobile": 4244420933}
    #     p7 = {"email": email, "password": "handstand", "first_name": user, "last_name": user, "mobile": 4244420933,
    #           "reebok_accept": 'fff'}
    #     p8 = {"email": email, "password": "handstand", "first_name": user, "last_name": user, "mobile": 4244420933,
    #           "reebok_accept": 999}
    #     p9 = {"email": 'dds', "password": "handstand", "first_name": user, "last_name": user, "mobile": 4244420933,
    #           "reebok_accept": 0}
    #     p10 = {"email": email1, "password": "handstand", "first_name": user, "last_name": user,
    #            "mobile": 42444209336666666, "reebok_accept": 0}
    #     p11 = {"email": email2, "password": "handstand", "first_name": user, "last_name": user, "mobile": 4244420933,
    #            "reebok_accept": 0}
    #     p12 = {"email": email3, "password": "handstand", "first_name": user, "last_name": user, "mobile": 4244420933,
    #            "reebok_accept": 1}
    #     s = p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p11, p12
    #     for i in s:
    #         r = requests.post(url, i, verify=False)
    #         print(Fore.BLUE + str(i))
    #
    #         if r.status_code != 200:
    #             print(r.headers["content-type"])
    #             print("[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
    #             print(Fore.GREEN + r.content.decode("utf-8"))
    #             time.sleep(5)
    #
    #         elif r.headers["content-type"] != 'application/json':
    #             print(
    #                 Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
    #             time.sleep(5)
    #         else:
    #             print("[SUCCESS]when calling[" + url + "]")
    #             info = r.content
    #             print(info)
    #             print(json.dumps(r.json(), indent=4))
    #             time.sleep(5)


    @lcc.test("My first test")
    def test_quizAPIClient(self):
        at_c=Base.test_accessTokenClient(self)
        at_t =Base.test_accessTokenTrainer(self)



        url = 'https://api-stage.handstandapp.com/api/v3/quiz'
        try:
            for i in range(1,5):
                p1 = i
                payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n" + str(p1) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
                headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",'authorization': "Bearer "+at_c,}
                print(Fore.BLUE + str(p1))
                r = requests.request("POST", url, data=payload, headers=headers,verify=False)
                if r.status_code != 200:
                    print(Fore.RED + r.headers["content-type"])
                    print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
                    print(Fore.RED + r.content.decode("utf-8"))

                elif r.headers["content-type"] != 'application/json':
                    print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
                else:
                    print("[SUCCESS]when calling[" + url + "]")
                    info = r.content
                    print(info)
                    print(json.dumps(r.json(), indent=4))
                    time.sleep(5)
        except:pass


if __name__ == "__main__":
    unittest.main()





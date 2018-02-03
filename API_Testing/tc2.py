from base import Base # importing base testcase
from colorama import *
import requests,json,time
import urllib3
urllib3.disable_warnings()

def test_loginClientAPI(self):
    url = 'https://api-stage.****ap.com/api/v3/login'

    p1 = {'email': 'APIddtest@gmail.com', 'password': 11111111, }
    p2 = {'password': 11111111, }
    p3 = {'email': 'APddItest@gmail.com'}
    p4 = {'email': 'randddom@gmail.com', 'password': '11111111', }
    p5 = {'email': 'APItddest@gmail.com', 'password': 'random', }

    s = p1, p2, p3, p4, p5
    for i in s:
        r = requests.post(url, i, verify=False)
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))

        elif r.headers["content-type"] != 'application/json':
            print(
                Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print(info)
            data = r.content
            d = json.loads(data.decode('utf-8'))

            print(json.dumps(r.json(), indent=4))
            time.sleep(5)

import requests,time

from colorama import *
import requests, json,sys,time
import unittest,os,time,sys,pymysql
from requests_toolbelt import MultipartEncoder
from datetime import datetime
from datetime import datetime
stamp = datetime.now().strftime("%Y-%m-%d%  %H:%m:%S %p")
stampdate = datetime.now().strftime("%Y-%m-%d% ")
stamptime = datetime.now().strftime("% %H:%m:%S %p")
emailstamp = datetime.now().strftime("%Y%m%d%H%M%S")
email="api_user_" + emailstamp + "@gmail.com"

print (stampdate)




class PostAPI_test(unittest.TestCase):


    def test_postapiTrainer_confirmbooking(self):
        r = requests.get(
            'https://stage.handstandapp.com/api/login?email=developer3%40handstandapp.com&password=handstand')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage.handstandapp.com/api/confirmbooking'
        params = {
            'access_token': at,
            'trainer_id': '9905',
            'booking_id': '412859',
            'status': 1,
            'flaf': 1}

        r = requests.post(url, params)

        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED +json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print(info)

            print(json.dumps(r.json(), indent=4))
        time.sleep(5)

    def test_postapiTrainer_uploadtoken(self):

        url = 'https://stage.handstandapp.com/api/uploadtoken'
        params = {
            'trainer_id': '9905',
            'device_token': 'dVoFDzwR8Ts%3AAPA91bE66Bxdch53JAUpnpJbtQeuXQpTiJPA2x4XCgei6HY9Xh43x3N9gSMFYqhNESknoaEFFqXb9aJsS1jGcZYxFsrltzxvn05MRst54d5pn6dTnICcDNPyRQyncCwcSixPd0Pbg0Ep',
            'device_type': 'android',
            'flag': 1}

        r = requests.post(url, params)

        if r.status_code != 200:
            print (Fore.RED + r.headers["content-type"])
            print (Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print (Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print ("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print (info)

            print (json.dumps(r.json(), indent=4))
        time.sleep(5)

    def test_postapiTrainer_availibility(self):

        r = requests.get(
            'https://stage.handstandapp.com/api/login?email=developer3%40handstandapp.com&password=handstand')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage-handstand-web.us-east-1.elasticbeanstalk.com/api/availibility'
        params = {
            'access_token': at,
            'day': '0',
            'time-slots': '05:00,05:30,06:00,06:30,07:00,07:30,08:00,08:30,09:00,09:30,10:00,10:30,11:00,11:30,12:00,12:30,13:00,13:30,14:00,14:30,15:00,15:30,16:00,16:30,17:00,17:30,18:00,18:30,19:00,19:30,20:00,20:30,21:00,21:30,22:00,22:30',
            'repeat': 1
        }

        r = requests.post(url, params, verify=False)

        if r.status_code != 200:
            print (Fore.RED + r.headers["content-type"])
            print (Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print (Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print ("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print (info)

            print (json.dumps(r.json(), indent=4))
        time.sleep(5)

    def test_postapiTrainer_bookclient(self):
        r = requests.get(
            'https://stage.handstandapp.com/api/login?email=developer3%40handstandapp.com&password=handstand')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage.handstandapp.com/api/bookclient?'
        params = {
            'access_token': at,
            'user_id': 10059,
            'starts_at': stamp ,
            'session_type': 'Boxing',
            'session_location': 'Los Angeles',
            'session_size': 'small-group',
            'flag': 1
        }

        r = requests.post(url, params, verify=False)

        if r.status_code != 200:
            print (Fore.RED + r.headers["content-type"])
            print (Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print (Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print ("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print (info)

            print (json.dumps(r.json(), indent=4))
        time.sleep(5)


    def test_postapiClient_cart(self):
        r = requests.get('https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=11111111')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage.handstandapp.com/api/cart?'
        params = {
            'access_token': at,
            'trainer_id': 9911,
            'date': 'Y-m-d',
            'time': '15:30',
            'session_class_type': 'Power Yoga',
            'location': 'Test, Ramaiah Layout, Bangalore, Karnataka, India'
        }

        r = requests.post(url, params, verify=False)

        if r.status_code != 200:
            print (Fore.RED + r.headers["content-type"])
            print (Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print (Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print ("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print (info)

            print (json.dumps(r.json(), indent=4))
        time.sleep(5)


    def test_postapiClient_book(self):


        r = requests.get(
            'https://stage.handstandapp.com/api/login?email=ClientAPI%40gmail.com&password=11111111')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']
        print (at)
        url = 'https://stage.handstandapp.com/api/book?'

        params = {
            'access_token': at,
            'workout_size': '1-On-1',
            'phone'       : 8557871111

        }

        r = requests.post(url, params, verify=False)

        if r.status_code != 200:
            print (Fore.RED + r.headers["content-type"])
            print (Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print (Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print ("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print (info)

            print (json.dumps(r.json(), indent=4))
        time.sleep(5)


    def test_postapiClient_uploadtoken(self):

        r = requests.get(
            'https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=11111111')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']
        print (at)
        url = 'https://stage.handstandapp.com/api/uploadtoken?'

        params = {
            'trainer_id': 9898,
             'device_token': 'cXyryG8fXic:APA91bHhTpftVevFuODQVcFUHLI02P0EPPMtyJFBoKyGQE-pJvjQW14pdZr4QCPg1S2LGj9wETG45Eh9QXyDoWyRW5QxLOAWOM-AoX3zZkokVXoDJZBDt8Yn5cPSEG7hJo1YUxfPdelL',
             'device_type': 'android',
             'flag':1

        }

        r = requests.post(url, params, verify=False)

        if r.status_code != 200:
            print (Fore.RED + r.headers["content-type"])
            print (Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print (Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print ("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print (info)

            print (json.dumps(r.json(), indent=4))
        time.sleep(5)


    def test_postapiClient_confirmbooking(self):

        r = requests.get('https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=11111111')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage.handstandapp.com/api/confirmbooking?'

        params =    {
                   'access_token': at,
                   'trainer_id': 62,
                    'booking_id': 396674 ,
                    'status' : 0 ,
                    'comments' : 'not available'

                    }


        r =  requests.post(url,params,verify=False)
        if r.status_code != 200:
            print (Fore.RED + r.headers["content-type"])
            print (Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print (Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print ("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print (info)
            print (json.dumps(r.json(), indent=4))
        time.sleep(5)




    def test_postapiClient_availibility(self):

        r = requests.get('https://stage.handstandapp.com/api/login?email=developer3%40handstandapp.com&password=handstand')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage.handstandapp.com/api/availibility?'

        params =    {
                     'access_token': at ,
                    'day' : 3 ,
                    'repeat' : 1 ,
                    'time-slots':'05:00,05:30,06:00,06:30,07:00,07:30,08:00,08:30,09:00,09:30,10:00,10:30,11:00,11:30,12:00,12:30,13:00,13:30,14:00,14:30,15:00,15:30,16:00,16:30,17:00,17:30,18:00,18:30,19:00,19:30,20:00,20:30,21:00,21:30,22:00,22:30'

        }


        r =  requests.post(url,params,verify=False)

        if r.status_code != 200:
            print (Fore.RED + r.headers["content-type"])
            print (Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print (Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print ("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print (info)
            print (json.dumps(r.json(), indent=4))
        time.sleep(5)




    def test_postapiClient_workouts(self):

        try:
            localhost = 'stage-handstand-web.clcfzghqjkhn.us-east-1.rds.amazonaws.com'
            host = 'stage-handstand-web.clcfzghqjkhn.us-east-1.rds.amazonaws.com'
            conn = pymysql.connect(host=host, port=3306, user='stagedb', passwd='handstand_stage', database='handstand')
            cur = conn.cursor()
            cur.execute("select id  from reservations where `requested_by`=0 ORDER BY RAND() LIMIT 0,1")
            for row in cur.fetchall():
                b = row[0]
            r1 = requests.get('https://stage.handstandapp.com/api/login?email=ClientAPI%40gmail.com&password=11111111')
            data = r1.content
            d = json.loads(data.decode('utf-8'))
            at = d['access_token']
            url = 'https://stage.handstandapp.com/api/workouts?'

            params = {
                'access_token': at,
                'sessionId': b

            }

            r = requests.post(url, params, verify=False)

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
                print(json.dumps(r.json(), indent=4))
            time.sleep(5)
        except:
            pass


    def test_postapiClient_ConfirmTrainerBooking(self):

        r = requests.get('https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=11111111')
        data = r.content

        d = json.loads(data.decode('utf-8'))
        at = d['access_token']
        print (at)
        print (stamp)
        url = 'https://stage.handstandapp.com/api/confirmtrainerbooking'
        params = {
            'access_token': at,
            'user_id': 10059,
            'booking_id': 466615,
            'status': 1,
        }

        r = requests.post(url, params, verify=False)

        if r.status_code != 200:
            print (Fore.RED + r.headers["content-type"])
            print (Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print (Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print ("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print (info)
            print (json.dumps(r.json(), indent=4))
        time.sleep(5)

    def test_postapiClient_bookCart(self):

        r = requests.get('https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=11111111')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage.handstandapp.com/api/bookCart'

        params = {
            'access_token': at,
            'date': stampdate,
            'location': '904 Huntington Ave, Boston, MA 02115',
            'session_class_type': 'Stretch & Recovery',
            'time': stamptime,
            'trainer_id': 9457,
            'workout_size': 'small-group',
            'comments': 'not available'

        }

        r = requests.post(url, params, verify=False)
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print(info)
            print(json.dumps(r.json(), indent=4))
        time.sleep(5)


    def test_postapiTrainer_createtrainer(self):

        r = requests.get('https://stage.handstandapp.com/api/login?email=developer3%40handstandapp.com&password=handstand')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage.handstandapp.com/api/createtrainer?'

        params = {
            'first_name': 'CHENNAREDDY',
            'last_name': 'BIRADAR,',
            'email': email,
            'phone': '7259692024',
            'birthday_month': '05',
            'birthday_day': 1,
            'birthday_year': 1989,
            'gender': 0,
            'password': 'handstand',
            'agree': 1

        }

        r = requests.post(url, params, verify=False)
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print(info)
            print(json.dumps(r.json(), indent=4))
        time.sleep(5)

    def test_postapiTrainer_trainerdetails(self):

        r = requests.get('https://stage.handstandapp.com/api/login?email=developer3%40handstandapp.com&password=handstand')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage.handstandapp.com/api/trainerdetails?'

        params = {
            'access_token': at,
            'zip_code': 90405,
            'distance': 5,
            'certifications': 8,
            'about': 'test',
            'experience': 8

        }

        r = requests.post(url, params, verify=False)
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print(info)
            print(json.dumps(r.json(), indent=4))
        time.sleep(5)

    def test_postapiTrainer_trainerspecs(self):

        r = requests.get(
            'https://stage.handstandapp.com/api/login?email=developer3%40handstandapp.com&password=handstand')
        data = r.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']

        url = 'https://stage.handstandapp.com/api/trainerspecs?'

        params = {
            'access_token': at,
            'specialties': '1,2,3'

        }

        r = requests.post(url, params, verify=False)
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print(info)
            print(json.dumps(r.json(), indent=4))
        time.sleep(5)



    def test_postapiTrainer_specs(self):
        url = 'https://stage.handstandapp.com/api/specs'

        params = {

        }

        r = requests.post(url, params, verify=False)
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print(info)
            print(json.dumps(r.json(), indent=4))
        time.sleep(5)



    def test_postapiTrainer_photoupload(self):
        img = open(os.getcwd() + '/chad.jpg', 'rb')

        r1 = requests.get(
            'https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=11111111')
        data = r1.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']
        print(at)
        url = 'https://stage.handstandapp.com/api/photo'

        m = MultipartEncoder(
            fields={'access_token': at,
                    'image': ('chad', img, 'text/image')}
        )

        r = requests.post('http://httpbin.org/post', data=m,
                          headers={'Content-Type': m.content_type})
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print("[SUCCESS]when calling[" + url + "]")
            print(json.dumps(r.json(), indent=4))
        time.sleep(5)

    def test_postapiTrainer_trainersettings(self):
        r1 = requests.get(
            'https://stage.handstandapp.com/api/login?email=developer3%40handstandapp.com&password=handstand')
        data = r1.content
        d = json.loads(data.decode('utf-8'))
        at = d['access_token']
        url = 'https://stage.handstandapp.com/api/trainersettings?'
        params = {
            'access_token': at,
            'first_name': 'handstand3',
            'last_name': 'developer3',
            'email': 'developer3@handstandapp.com',
            'phone': 3107523148,
            'birthday_month': 5,
            'birthday_day': 1,
            'birthday_year': 1989,
            'flag': 1}

        r = requests.post(url, params)

        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':
            print(Fore.RED + "[ERROR] when calling [" + url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print("[SUCCESS]when calling[" + url + "]")
            info = r.content
            print(info)

            print(json.dumps(r.json(), indent=4))
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()
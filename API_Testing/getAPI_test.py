import requests
import time,ssl
import requests, json,sys
import unittest,os,time,sys
from datetime import datetime
from colorama import *
import csv,re




class GetAPI_test(unittest.TestCase):


    # def test_searchAPI_multipleZipcode(self):
    #     """
    #      trainerslist?
    #
    #     :return:
    #     """
    #
    #     filename = 'zip.csv'
    #
    #     with open(filename, 'rt') as f:
    #         mycsv = csv.reader(f)
    #         mycsv = list(mycsv)
    #         for i in mycsv:
    #             src = ", ".join(i)
    #             get_url = 'https://stage.handstandapp.com/api/search?zip_code=' + src + '&date=2017-12-13&time=10:00:00&goal=Kids%20Yoga,Zumba%20&%20Dance%20Fit,Tennis'
    #             print(get_url)
    #             host_address = 'https://stage.handstandapp.com'
    #             r = requests.get(get_url)
    #             try:
    #                 a = r.json()
    #             except:
    #                 pass
    #
    #             if r.status_code != 200 and r.status_code != 204:
    #                 print(Fore.RED + r.headers["content-type"])
    #                 print(Fore.RED + "[ERROR] when calling[" + get_url + "] got back HTTP response code:" + str(r.status_code))
    #
    #             elif r.headers["content-type"] != 'application/json': \
    #                 print(Fore.GREEN + "[No Content] when calling [" + get_url + "] got back non JSON data:" + r.headers['content-type'])
    #             else:
    #                 print(Fore.GREEN + "[SUCCESS]when calling[" + get_url + "]", a)
    #                 try:
    #                     for i in range(0, len(a['data'])):
    #                         trainer_zip = a['data'][i]['zip']
    #                         dst = a['data'][i]['max_distance']
    #                         t_zip = (trainer_zip)
    #                         # print(t_zip)
    #                         url1 = "http://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+t_zip+"&destinations="+src+"/mile"
    #                         r1 = requests.get(url1)
    #                         a1 = r1.json()
    #                         b = a1['rows'][0]['elements'][0]['distance']['text']
    #                         b1 = b[0:4].strip()
    #                         c = b1
    #                         try:
    #                             if int(dst) >= float(c):
    #                                 print(Fore.BLUE + 'Valid trainer list', '--->', 'Trainer_ID-', a['data'][i]['id'],'  ' 'MAX_DST-', dst, '  ' 'ACTUAL_DST-', c, '   ' 'ZIPCODE-', t_zip,  '   ' 'DST_ZIPCODE-', src ,)
    #                             else:
    #                                 print(Fore.RED + ' Wrong trainer list', '--->', 'Trainer_ID-', a['data'][i]['id'],'  ' 'MAX_DST-', dst, '  ' 'ACTUAL_DST-', c, '   ' 'ZIPCODE-', t_zip,  '   ' 'DST_ZIPCODE-', src ,)
    #                         except:
    #                             pass
    #                 except:pass
    def test_searchAPI_singlezipcode(self):
        """
         This script to find valid and invalid Trainer list based on mile and zipcode

        :return:
        """

        get_url = 'https://api-stage.handstandapp.com/api/v2/search?zip_code=90405&lng=-118.413549&lat=34.070766&date=2018-12-25&time=22:30:00&goal=Boxing,Kids%20Yoga,Bootcamp'



        host_address = 'https://stage.handstandapp.com'
        r = requests.get(get_url)
        a=r.json()
        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + get_url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':\
            print(Fore.RED + "[ERROR] when calling [" + get_url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            print(Fore.GREEN + "[SUCCESS]when calling[" + get_url + "]")
            for i in range(1, len(a['data'])):
                trainer_zip= a['data'][i]['zip']
                dst=a['data'][i]['max_distance']
                t_zip=(trainer_zip)
                url1 = "http://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+t_zip+"&destinations=90405/mile"
                r1 = requests.get(url1)

                a1 = r1.json()
                b = a1['rows'][0]['elements'][0]['distance']['text']
                b1 = b[0:4].strip()
                c=b1
                try:
                    if int(dst)>=int(c):
                        print(Fore.BLUE+'Valid trainer list','--->','Trainer_ID-',a['data'][i]['id'],'   ' 'MAX_DST-',dst,'  ' 'ACTUAL_DST-', c,'   ' 'ZIPCODE-', t_zip,)
                    else:
                       print(Fore.RED+' Wrong trainer list','--->','Trainer_ID-',a['data'][i]['id'],'   ' 'MAX_DST-',dst,'  ' 'ACTUAL_DST-', c,'   ' 'ZIPCODE-', t_zip,)
                except:pass


    def test_searchAPIMobile(self):
        """
         trainerslist?

        :return:
        """





        get_url='https://api-stage.handstandapp.com/api/v2/search?zip_code=90405&date=2017-11-13&time=10:00:00&goal=Kids%20Yoga,Zumba%20&%20Dance%20Fit,Tennis'
        #get_url = 'https://stage.handstandapp.com/api/trainerslist?date=2017-12-02&goal=Weight%20Loss%20Coaching&gymId=&gymType=&time=%2708%3A30%3A00%27%20and%20%2708%3A30%3A00%27&zipcode=90405'

        host_address = 'https://stage.handstandapp.com'
        r = requests.get(get_url)
        a=r.json()

        #print(len(a['data']))
        # for i in range(0, len(a['data'])):
        #     print(len(a['data'][i]['zip']))


        if r.status_code != 200:
            print(Fore.RED + r.headers["content-type"])
            print(Fore.RED + "[ERROR] when calling[" + get_url + "] got back HTTP response code:" + str(r.status_code))
            print(Fore.RED + json.dumps(r.json(), indent=4))
        elif r.headers["content-type"] != 'application/json':\
            print(Fore.RED + "[ERROR] when calling [" + get_url + "] got back non JSON data:" + r.headers['content-type'])
        else:
            #print(Fore.GREEN + "[SUCCESS]when calling[" + get_url + "]", a)
            for i in range(0, len(a['data'])):
                x = i
                #print(a[x]['max_distance'])
                #print(a[x]['zipcode'])
                trainer_zip= a['data'][i]['zip']
                t_zip=(trainer_zip)

                #print(t_zip)
                url1="https://www.zipcodeapi.com/rest/Wik66snC9rP7LXvhYqz6eZu83UPfkSPhbanhDKUMbKUXHpeGQOM5NheQb36vVWM6/distance.json/"+t_zip+"/90405/mile"
                r1 = requests.get(url1)
                a1 = r1.json()
                c=(a1['distance'])

                if (a['data'][i]['max_distance'])>=c:
                    print(Fore.BLUE + 'Valid trainer list', '--->','id-',a['data'][i]['id'],'   ' 'max_dst-',(a['data'][i]['max_distance']),'  ' 'actual_dst-', c,'   ' 'zipcode-', t_zip,)
                else:
                    print(Fore.RED  + 'Wrong trainer list', '--->','id-',a['data'][i]['id'],'   ' 'max_dst-',(a['data'][i]['max_distance']),'  ' 'actual_dst-', c,'  ' 'zipcode-', t_zip,)



    def test_login_APIValidation(self):
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
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]",a)


                    elif ", ".join(a['errors']) == 'The email must be a valid email address.':
                        assert r.status_code == 422
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'The email must be a valid email address.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)

                    elif ", ".join(a['errors']) == 'Email or password was incorrect.':
                        assert r.status_code == 403
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'Email or password was incorrect.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)
                    elif ", ".join(a['errors']) == 'The password field is required.':
                        assert r.status_code == 422
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'The password field is required.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)
                    elif ", ".join(a['errors']) == 'Email or password was incorrect.':
                        assert r.status_code == 403
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'Email or password was incorrect.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)
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

    def test_getapi_Trainer(self):
        """
        gymlocations,gymregions,profile,profile?,TrainerAppointments,getavailibility,listclients,globalTrainersSpeciality,login,workouts

        :return:
        """


        r1 = requests.get('https://stage.handstandapp.com/api/login?email=developer3%40handstandapp.com&password=handstand')
        data = r1.content
        d = json.loads(data.decode('utf-8'))
        get_urls = ['https://stage.handstandapp.com/api/gymlocations', 'http://stage.handstandapp.com/api/gymregions',
                    'https://stage.handstandapp.com/api/profile?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/TrainerAppointments?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/getavailibility?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/booknotification?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/listclients?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/globalTrainersSpecialityInfo?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/workouts?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/TrainersSpecialityInfo?access_token=' + d['access_token']
                    ]

        host_address = 'https://stage.handstandapp.com'
        for rest_url in get_urls:
            r = requests.get(rest_url)
            time.sleep(4)
            try:
                a = r.json()
                if r.status_code != 200:

                    print (Fore.RED + r.headers["content-type"])
                    print (Fore.RED + "[ERROR] when calling["+ rest_url + "] got back HTTP response code:" + str(r.status_code))
                    print(Fore.RED + json.dumps(r.json(), indent=4))
                elif r.headers["content-type"]!= 'application/json':
                    print (Fore.RED +"[ERROR] when calling [" + rest_url +"] got back non JSON data:" + r.headers['content-type'])
                else:
                    print ('\n')
                    print (
                    '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    print ('\n')
                    print(Fore.GREEN + "[SUCCESS]when calling[" + rest_url + "]", a)
                    print(json.dumps(r.json(), indent=4))
            except:
                pass

    def test_getapi_TrainerValidationerror(self):
        """
        gymlocations,gymregions,profile,profile?,TrainerAppointments,getavailibility,listclients,globalTrainersSpeciality,login,workouts

        :return:
        """


    get_urls = [
        'https://stage.handstandapp.com/api/profile?access_token=',
        'https://stage.handstandapp.com/api/TrainerAppointments?access_token=',
        'https://stage.handstandapp.com/api/getavailibility?access_token=',
        'https://stage.handstandapp.com/api/listclients?access_token=',
        'https://stage.handstandapp.com/api/globalTrainersSpecialityInfo?access_token=',
        'https://stage.handstandapp.com/api/workouts?access_token=',
        'https://stage.handstandapp.com/api/TrainersSpecialityInfo?access_token='
        'https://stage.handstandapp.com/api/booknotification?access_token='  ,
        'https://stage.handstandapp.com/api/profile?access_token=gg',
        'https://stage.handstandapp.com/api/TrainerAppointments?access_token=gg',
        'https://stage.handstandapp.com/api/getavailibility?access_token=gg',
        'https://stage.handstandapp.com/api/listclients?access_token=gg',
        'https://stage.handstandapp.com/api/globalTrainersSpecialityInfo?access_token=gg',
        'https://stage.handstandapp.com/api/workouts?access_token=gg',
        'https://stage.handstandapp.com/api/TrainersSpecialityInfo?access_token=gg'
    ]

    host_address = 'https://stage.handstandapp.com'
    for rest_url in get_urls:
        r = requests.get(rest_url)
        time.sleep(4)
        try:

            if r.status_code != 200:
                a = r.json()
                if ", ".join(a['errors']) == 'No access token.':
                    assert str(r.status_code) == '403'
                    assert r.headers["content-type"] == 'application/json'
                    assert a['result'] == 'error'
                    assert ", ".join(a['errors']) == 'No access token.'
                    print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)
                else:
                    assert str(r.status_code) == '403'
                    assert r.headers["content-type"] == 'application/json'
                    assert a['result'] == 'error'
                    assert ", ".join(a['errors']) == 'Invalid access token.'
                    print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)

            elif r.headers["content-type"] != 'application/json':
                print(Fore.RED + "[ERROR] when calling [" + rest_url + "] got back non JSON data:" + r.headers[
                    'content-type'])
            else:
                print('\n')
                print(
                    '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('\n')
                print(Fore.RED+"[FAIL]when calling[" + rest_url + "]")
                info = r.content
                print(info)
                print(json.dumps(r.json(), indent=4))
        except:
            pass

    def test_getapi_user(self):
        """
         booknotification,review,cards,logout,login?,passport,trainerslist?date,sendtoalltrainers

        :return:
        """


        r1 = requests.get(
            'https://stage.handstandapp.com/api/login?email=handstandtest78%40gmail.com&password=11111111')
        data = r1.content
        d = json.loads(data.decode('utf-8'))

        get_urls = [
                    'https://stage.handstandapp.com/api/passport','https://stage.handstandapp.com/api/copy',
                    'https://stage.handstandapp.com/api/reviews?id=4070',
                    'https://stage.handstandapp.com/api/trainersInfo?id=9457',
                    'https://stage.handstandapp.com/api/booknotification?access_token=' + d['access_token'] ,
                    'https://stage.handstandapp.com/api/review?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/cards?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/workouts?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/profile?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/logout?access_token=' + d['access_token'],
                    'https://stage.handstandapp.com/api/login?email=handstandtest8%40gmail.com&password=11111111',
                    'https://stage.handstandapp.com/api/get_passports'
                    'https://stage.handstandapp.com/api/trainerslist?date=2017-12-02&goal=Weight%20Loss%20Coaching&gymId=&gymType=&time=%2708%3A30%3A00%27%20and%20%2708%3A30%3A00%27&zipcode=90404'
                    'https://stage.handstandapp.com/api/sendtoalltrainers',
                    ]
        host_address = 'https://stage.handstandapp.com'
        for rest_url in get_urls:
            r = requests.get(rest_url)
            time.sleep(4)
            try:
                a=r.json()
                if r.status_code != 200:
                    print(Fore.RED + r.headers["content-type"])
                    print(Fore.RED + "[ERROR] when calling[" + rest_url + "] got back HTTP response code:" + str(
                        r.status_code))
                    print(Fore.RED + json.dumps(r.json(), indent=4))
                elif r.headers["content-type"] != 'application/json':
                    print(Fore.RED + "[ERROR] when calling [" + rest_url + "] got back non JSON data:" + r.headers[
                        'content-type'])
                else:
                    print('\n')
                    print(
                        '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    print('\n')
                    print(Fore.GREEN + "[SUCCESS]when calling[" + rest_url + "]", a)
                    print(json.dumps(r.json(), indent=4))
            except:
                pass

    def test_getapi_user_accesstokenValidation(self):
        """
         booknotification,review,cards,logout,login?,passport,trainerslist?date,sendtoalltrainers

        :return:
        """



        get_urls = [

            'https://stage.handstandapp.com/api/reviews?id=470',
            'https://stage.handstandapp.com/api/trainersInfo?id=ff',
            'https://stage.handstandapp.com/api/booknotification?access_token=',
            'https://stage.handstandapp.com/api/review?access_token=',
            'https://stage.handstandapp.com/api/cards?access_token=',
            'https://stage.handstandapp.com/api/workouts?access_token=',
            'https://stage.handstandapp.com/api/profile?access_token=',
            'https://stage.handstandapp.com/api/logout?access_token=', ]
        get_urls1 = [

            'https://stage.handstandapp.com/api/booknotification?access_token=g',
            'https://stage.handstandapp.com/api/review?access_token=g',
            'https://stage.handstandapp.com/api/cards?access_token=g',
            'https://stage.handstandapp.com/api/workouts?access_token=g',
            'https://stage.handstandapp.com/api/profile?access_token=g',
            'https://stage.handstandapp.com/api/logout?access_token=g',

        ]
        host_address = 'https://stage.handstandapp.com'
        for rest_url in get_urls:
            r = requests.get(rest_url)
            time.sleep(4)
            try:
                if r.status_code != 200:
                    a = r.json()
                    if r.status_code == 404:
                        assert r.status_code == 404
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'Could not find this trainer'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)
                    elif r.status_code == 403:
                        assert r.status_code == 403
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'No access token.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)
                    else:
                        pass
                elif r.headers["content-type"] != 'application/json':
                    print(Fore.RED + "[ERROR] when calling [" + rest_url + "] got back non JSON data:" + r.headers[
                        'content-type'])
                else:
                    print('\n')
                    print(
                        '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    print('\n')
                    print(Fore.RED+"[FAIL]when calling[" + rest_url + "]")

            except:
                pass
        for rest_url in get_urls1:
            r = requests.get(rest_url)
            time.sleep(4)
            try:
                if r.status_code != 200:
                    a = r.json()
                    if r.status_code == 403:
                        assert r.status_code == 403
                        assert r.headers["content-type"] == 'application/json'

                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'Invalid access token.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)
                    else:
                        pass
                elif r.headers["content-type"] != 'application/json':
                    print(Fore.RED + "[ERROR] when calling [" + rest_url + "] got back non JSON data:" + r.headers[
                        'content-type'])
                else:
                    print('\n')
                    print(
                        '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    print('\n')
                    print(Fore.RED+"[FAIL]when calling[" + rest_url + "]")

            except:
                pass

    def test_getapi_userrainerslist(self):
        """
         trainerslist?

        :return:
        """

        get_urls = [
            'https://stage.handstandapp.com/api/trainerslist?date=&goal=Weight%20Loss%20Coaching&gymId=&gymType=&time=%2708%3A30%3A00%27%20and%20%2708%3A30%3A00%27&zipcode=90404',
            'https://stage.handstandapp.com/api/trainerslist?date=999&goal=Weight%20Loss%20Coaching&gymId=&gymType=&time=%2708%3A30%3A00%27%20and%20%2708%3A30%3A00%27&zipcode=90404',
            'https://stage.handstandapp.com/api/trainerslist?date=&goal=&gymId=&gymType=&time=%2708%3A30%3A00%27%20and%20%2708%3A30%3A00%27&zipcode=90404',
            'https://stage.handstandapp.com/api/trainerslist?date=2017-12-02&goal=008&gymId=&gymType=&time=%2708%3A30%3A00%27%20and%20%2708%3A30%3A00%27&zipcode=90404',

            'https://stage.handstandapp.com/api/trainerslist?date=&goal=& gymId=&gymType=&time=&zipcode=',
            'https://stage.handstandapp.com/api/trainerslist?date=2017-12-02&goal=Weight%20Loss%20Coaching&gymId=&gymType=&time=&zipcode=90404',
            'https://stage.handstandapp.com/api/trainerslist?date=2017-12-02&goal=Weight%20Loss%20Coaching&gymId=&gymType=&time=kkk&zipcode=90404',

            'https://stage.handstandapp.com/api/trainerslist?date=2017-12-02&goal=Weight%20Loss%20Coaching&gymId=&gymType=&time=%2708%3A30%3A00%27%20and%20%2708%3A30%3A00%27&zipcode=',
            'https://stage.handstandapp.com/api/trainerslist?date=2017-12-02&goal=Weight%20Loss%20Coaching&gymId=&gymType=&time=%2708%3A30%3A00%27%20and%20%2708%3A30%3A00%27&zipcode=hvvv',

        ]

        host_address = 'https://stage.handstandapp.com'
        for rest_url in get_urls:
            r = requests.get(rest_url)
            time.sleep(4)
            try:
                if r.status_code != 200:
                    a = r.json()

                    if ", ".join(a['errors']) == 'The date field is required.':
                        assert r.status_code == 422
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'The date field is required.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)

                    elif ", ".join(a['errors']) == 'The date field is invalid.':
                        assert r.status_code == 422
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'The date field is invalid.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)

                    elif ", ".join(a['errors']) == 'The goal field is required.':
                        assert r.status_code == 422
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'The goal field is required.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)

                    elif ", ".join(a['errors']) == 'The goal field is invalid.':
                        assert r.status_code == 422
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'The goal field is invalid.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)

                    elif ", ".join(a['errors']) == 'The time field is required.':
                        assert r.status_code == 422
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'The time field is required.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)

                    elif ", ".join(a['errors']) == 'The time field is invalid.':
                        assert r.status_code == 422
                        assert r.headers["content-type"] == 'application/json'
                        a = r.json()
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'The time field is invalid.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)

                    elif ", ".join(a['errors']) == 'The zipcode field is required.':
                        assert r.status_code== 422
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ",".join(a['errors']) == 'The zipcode field is required.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)

                    elif ", ".join(a['errors']) == 'The zipcode field is invalid.':
                        assert r.status_code == 422
                        assert r.headers["content-type"] == 'application/json'
                        assert a['result'] == 'error'
                        assert ", ".join(a['errors']) == 'The zipcode field is invalid.'
                        print(Fore.GREEN +"[PASS]when calling[" + rest_url + "]", a)
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
                    print(Fore.RED+"[FAIL]when calling[" + rest_url + "]")

            except:
                pass





if __name__ == "__main__":
    unittest.main()
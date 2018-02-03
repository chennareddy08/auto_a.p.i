import requests
import time,ssl
import csv,re

import requests, json,sys
import unittest,os,time,sys
from datetime import datetime
from colorama import *
import unittest,os,time,sys,pymysql



class GetAPI_test(unittest.TestCase):

    def test_searchAPIMobile(self):
        """
         trainerslist?

        :return:
        """





        get_url='https://stage.handstandapp.com/api/search?zip_code=90405&date=2017-11-13&time=10:00:00&goal=Kids%20Yoga,Zumba%20&%20Dance%20Fit,Tennis'
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










if __name__ == "__main__":
    unittest.main()
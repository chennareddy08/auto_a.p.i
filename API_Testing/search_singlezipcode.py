import requests, json,sys
import unittest,os,time
from datetime import datetime
from colorama import *

class GetAPI_test(unittest.TestCase):

    def test_searchAPI_singlezipcode(self):
        """
         This script to find valid and invalid Trainer list based on mile and zipcode

        :return:
        """

        get_url = 'https://api-stage.handstandapp.com/api/v3/search?lat=34.009746&lng=-118.4659576&zip_code=90405 &date=2018-12-25&time=22:30:00&goal=Boxing,Kids%20Yoga,Bootcamp'

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

                print(trainer_zip)
                t_zip=(trainer_zip)
                url1="https://www.zipcodeapi.com/rest/RVpD1lW30LHDHbyXZnG7ex5CYRHmMcaD7zg8UdcUYTxG56E4tkbIRhlP83cUfmym/distance.json/"+t_zip+"/90405/mile"
                r1 = requests.get(url1)
                a1 = r1.json()
                c=(a1['distance'])
                if int(a['data'][i]['max_distance'])>=int(c):
                    print(Fore.BLUE+'Valid trainer list','--->','Trainer_ID-',a['data'][i]['id'],'   ' 'MAX_DST-',(a['data'][i]['max_distance']),'  ' 'ACTUAL_DST-', c,'   ' 'ZIPCODE-', t_zip,)
                else:
                    print(Fore.RED+' Wrong trainer list','--->','Trainer_ID-',a['data'][i]['id'],'   ' 'MAX_DST-',(a['data'][i]['max_distance']),'  ' 'ACTUAL_DST-', c,'   ' 'ZIPCODE-', t_zip,)


if __name__ == "__main__":
    unittest.main()
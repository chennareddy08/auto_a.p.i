import requests
import time,ssl
import requests, json,sys
import unittest,os,time,sys
from datetime import datetime
from colorama import *
import csv,re



class GetAPI_test(unittest.TestCase):

    def test_searchAPI_multipleZipcode(self):
        """
         trainerslist?

        :return:
        """

        filename = 'zip.csv'

        with open(filename, 'rt') as f:
            mycsv = csv.reader(f)
            mycsv = list(mycsv)
            for i in mycsv:
                src = ", ".join(i)
                get_url = 'https://stage.handstandapp.com/api/search?zip_code=' + src + '&date=2017-12-13&time=10:00:00&goal=Kids%20Yoga,Zumba%20&%20Dance%20Fit,Tennis'
                print(get_url)
                host_address = 'https://stage.handstandapp.com'
                r = requests.get(get_url)
                try:
                    a = r.json()
                except:
                    pass

                if r.status_code != 200 and r.status_code != 204:
                    print(Fore.RED + r.headers["content-type"])
                    print(Fore.RED + "[ERROR] when calling[" + get_url + "] got back HTTP response code:" + str(r.status_code))

                elif r.headers["content-type"] != 'application/json': \
                    print(Fore.GREEN + "[No Content] when calling [" + get_url + "] got back non JSON data:" + r.headers['content-type'])
                else:
                    print(Fore.GREEN + "[SUCCESS]when calling[" + get_url + "]", a)
                    try:
                        for i in range(0, len(a['data'])):
                            trainer_zip = a['data'][i]['zip']
                            dst = a['data'][i]['max_distance']
                            t_zip = (trainer_zip)
                            # print(t_zip)
                            url1 = "http://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+t_zip+"&destinations="+src+"/mile"
                            r1 = requests.get(url1)
                            a1 = r1.json()
                            b = a1['rows'][0]['elements'][0]['distance']['text']
                            b1 = b[0:4].strip()
                            c = b1
                            try:
                                if int(dst) >= float(c):
                                    print(Fore.BLUE + 'Valid trainer list', '--->', 'Trainer_ID-', a['data'][i]['id'],'  ' 'MAX_DST-', dst, '  ' 'ACTUAL_DST-', c, '   ' 'ORIGINS_ZIPCODE-', t_zip, '   ' 'DST_ZIPCODE-', src )
                                else:
                                    print(Fore.RED + ' Wrong trainer list', '--->', 'Trainer_ID-', a['data'][i]['id'],'  ' 'MAX_DST-', dst, '  ' 'ACTUAL_DST-', c, '   ' 'ORIGINS_ZIPCODE-', t_zip, '   ' 'DST_ZIPCODE-', src,)
                            except:
                                pass
                    except:pass
if __name__ == "__main__":
    unittest.main()
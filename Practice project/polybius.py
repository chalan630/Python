'''
@Descripttion: 穷举法破解polybius密码
@Author: chalan630
@Date: 2020-01-20 20:45:26
@LastEditTime : 2020-01-20 23:32:17
'''
import os
from itertools import permutations
def AllRange(listx=[]): #全排列
    ret = []
    for x in list(permutations(listx)):
        ret.append(list(x))
    return ret

os.system('cls')
ks = AllRange(['a','e','i','o','u'])
# 密文
crypo = 'ouauuuoooeeaaiaeauieuooeeiea'
# 密码表
table = 'abcdefghiklmnopqrstuvwxyz'
for k in ks:
    a = "".join(k)
    print('\n01234->',a,'  |',end='')
    for i in range(0,27,2):
        x=a.find(crypo[i])*5 + a.find(crypo[i+1])
        print(table[x],end='')

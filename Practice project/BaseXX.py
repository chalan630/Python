'''
@Descripttion: 
@Author: chalan630
@Date: 2020-01-20 15:51:32
@LastEditTime : 2020-01-20 20:33:51
'''
# coding:utf-8

table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def BaseXX_encode(words):
    # 字符转化为二进制列表
    bin_str = []    
    for i in words:
        temp = str(bin(ord(i))).replace('0b', '')
        bin_str.append('{:0>8}'.format(temp))
    # print(bin_str)
    outputs = ""
    # 不够3的倍数，需要补的次数
    nums = 0
    while bin_str:
        # 3*8 -> 4*6 不够补0
        raw_list = bin_str[:3]
        if len(raw_list) < 3:
            nums = 3 - len(raw_list)
            for i in range(0, nums):
                raw_list.append('00000000')
        raw_str = "".join(raw_list)
        inter_list = []
        for i in range(0, 4):
            inter_list.append(int(raw_str[i*6:(i+1)*6], 2))
        # 对照密码表输出
        for i in inter_list:
            if i:
                outputs += table[i]
            else:
                outputs += '='
        bin_str = bin_str[3:]
    print("Encrypted String:\n%s"%outputs)


def BaseXX_decode(words):
    bin_str = []
    # 将字符串转化为2进制
    for i in words:
        if i != '=':
            temp = str(bin(table.index(i))).replace('0b', '')
            bin_str.append('{:0>6}'.format(temp))
    outputs = ""
    while bin_str:
        raw_list = bin_str[:4]
        raw_str = "".join(raw_list)
        nums = len(raw_str) % 8
        if(nums!=0):
            raw_str = raw_str[0:-nums]
        for i in range(0, int(len(raw_str)/8)):
            outputs += chr(int(raw_str[i*8:(i+1)*8], 2))
        bin_str = bin_str[4:]
    print("Decrypted String:\n%s "%outputs)


print()
print("     *************************************")
print("     *    (1)encode         (2)decode    *")	
print("     *************************************")
print()

num = input("Please select the operation:\n")
if num == '1':
    words = input("Please input a string that you want to encrypted:\n")
    BaseXX_encode(words)
elif num == '2':
    words = input("Please input a string that you want to decrypted:\n")
    BaseXX_decode(words)
else:
    print("What do you want?")
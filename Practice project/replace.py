'''
@Descripttion: 
@version: 
@Author: chalan630
@Date: 2020-05-11 14:55:08
@LastEditTime: 2020-05-11 16:48:29
'''

dict = "!@#$%^&*()"
raw_str = "^b^%&(^@^f^!&@^$%f^%^e^#"
output = ''

for i in raw_str:
    output += str(dict.find(i) + 1) if dict.find(i) > -1 else i


print(bytes.fromhex(output))        # 16进制 str 转 byte
print('flag{' + str(bytes.fromhex(output), encoding='utf-8') + '}')

# >>> a = '中文'
# >>> a
# '中文'
# >>> type(a)
# <class 'str'>
# >>> bytes(a, encoding='utf-8')
# b'\xe4\xb8\xad\xe6\x96\x87'
# >>> b = bytes(a, encoding='utf-8')
# >>> type(b)
# <class 'bytes'>
# >>> str(b)
# "b'\\xe4\\xb8\\xad\\xe6\\x96\\x87'"
# >>> str(b, encoding='utf-8')
# '中文'
# >>> b
# b'\xe4\xb8\xad\xe6\x96\x87'
# >>> c = str(b)
# >>> c
# "b'\\xe4\\xb8\\xad\\xe6\\x96\\x87'"
# >>> c.replace('\\x','')
# "b'e4b8ade69687'"
# >>> c.replace('\\x','')[2:]
# "e4b8ade69687'"
# >>> c.replace('\\x','')[2:-1]
# 'e4b8ade69687'
# >>> d = c.replace('\\x','')[2:-1]
# >>> d
# 'e4b8ade69687'
# >>> bytes.fromhex(d)
# b'\xe4\xb8\xad\xe6\x96\x87'
# >>> str(bytes.fromhex(d), encoding='utf-8')
# '中文'
# >>>
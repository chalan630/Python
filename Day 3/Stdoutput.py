#! /usr/bin/env/ python3
'''
@Description: 输出格式美化
@version: 
@Author: chalan630
@Date: 2019-12-25 16:46:15
@LastEditTime : 2020-02-08 15:22:58
'''

# PartⅠ
num = 86                 
print(repr(num).rjust(4))   # rjust()方法返回一个原字符右对齐，并使用空格填充至长度width的新字符串
# output:  86
print(str(num).zfill(5))    # zfill()会在数字的左边填充0
# output:00086

# Part Ⅱ
str1 = "\tHello world"
print(str(str1))            # 用于将对象转化为适于人阅读的字符串的形式
# output:        Hello world
print(repr(str1))           # 用于将对象转化为可供解释器读取的字符串的形式
# output:'\tHello world'
print(chr(str1))            # 将一个整数转化为字符，整数为字符的ASCII编码
print(eval(str1))           # 将字符串str当做表达式进行求值，并返回计算结果
# 字符串字面值可以跨行连续输入。一种方式是用三重引号："""...""" 或 '''...'''。
# 字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可
print("""\
    Usage: thingy [OPTIONS]
    -h                      Display this usage message
    -H hostname             Hostname to connect to
    """)

# Part Ⅲ
name = '我的博客'
site = 'www.baidu.com'
print('{1}网址：{0}'.format(name, site))                                       # 使用位置参数
# output:www.baidu.com网址：我的博客
print('{name}网址： {site}'.format(name='我的博客', site='www.baidu.com'))      # 使用关键字参数

# 可选项`:`和格式标识符可以跟着字段名。这就允许对值进行更好的格式化
import math
print('常量PI的值近似为{0:.3f}'.format(math.pi))                                # 将Pi保留到小数点后三位
print('{0:10}==>{1:10d}'.format('有一个数字', 666))                             # 保证该域至少有这么多的宽度
print('{:>10}'.format(12))                                                    # ^、<、>分别是居中、左对齐、右对齐，后面带宽度
print('{:0>10}'.format(12))                                                   # :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print('{:b}'.format(12))                                                      # b、d、o、x分别是二进制、十进制、八进制、十六进制
print("{:,}".format(1234567890))                                              # 千位分隔符

# f-strings
name = "Q1mi"
age = 18
print(f"My name is {name}.I'm {age}")


# 传入一个字典, 然后使用方括号`[]`来访问键值
table = {'Google': 1, 'Baidu': 2, 'Taobao': 3}
print('Baidu: {0[Baidu]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# output:Baidu: 2; Google: 1; Taobao: 3

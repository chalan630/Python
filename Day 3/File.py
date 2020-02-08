'''
@Description: Day3的文件操作
@Author: chalan630
@Date: 2019-12-26 09:20:10
@LastEditTime : 2020-02-08 15:22:49
'''
# 打开一个文件
f = open("open.txt", "w")
# 文件写入操作
f.write("Python是一个非常好的语言。\n是的，的确非常好！！\n")
# 关闭打开的文件
f.close()

# 调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回
f.read()

# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。
# f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
f.readline()

# f.readlines() 将返回该文件中包含的所有行。
# 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
f.readlines()

# 将 string 写入到文件中, 然后返回写入的字符数。
num = f.write("string")

'''
@Description: 列表相关操作
@Author: chalan630
@Date: 2019-12-25 14:23:08
@LastEditTime : 2020-02-08 15:22:05
'''
bicycles = ['trek', 'cannondale', 'redline', 'speciailized']

# 输出指定索引的列表元素
print(bicycles[1])

# 不知道列表长度的情况下，输出最后一个元素
print(bicycles[-1])

# 在列表中增加新元素
bicycles.append('honda')

# 修改列表元素
bicycles[0] = 'yamaha'

# 在列表中插入元素
bicycles.insert(0, 'suzuki')

# 删除列表中元素
del bicycles[1]

# 根据值删除列表中元素
bicycles.remove('suzuki')

# 对列表进行排序
bicycles.sort()                     # 当前列表永久排序
bicycles.sort(reverse=True)         # 当前列表逆序排序
sorted(bicycles)                    # 当前列表临时排序

# 对列表进行反转操作
bicycles.reverse()

# 输出列表长度
len(bicycles)

# 生成数字(1, 2, 3, 4)
range(1, 5)
range(1, 10, 2)                     # 步长为2

# 列表生成式
squares = [value**2 for value in range(1, 11)]
print(squares)

# 练习1 打印1~20
for i in range(1, 21):
    print(i, end=' ')

# 尝试只用一行实现练习1
print(' '.join(list(str(i) for i in range(1, 21))))

# 只用一行代码实现打印1~20的奇数
print(' '.join(list(str(i) for i in range(1, 21) if i % 2 != 0)))

# 列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
players[0:3]                       # 列表中1~3
players[1:4]                       # 列表中2~4
players[:4]                         # 列表中从开头到第三个
players[2:]                         # 列表中第二个到结尾
players[-3:]                        # 列表上最后三个
players[::-1]                      
# 步进为-1   意为逆序(这种技巧对字节串和ASCII字符有用，对已经编码成UTF-8字节串的Unicode字符来说，无法奏效)

# ★★★复制列表★★★
list2 = [1,2,3,4]
list1 = list2                       # 类比指针和地址(将list2赋给list1,并不是将list2的副本存储到list1)
list1 = list2[:]                    # 复制列表浅拷贝
list1.copy(list2)                   # 与上句意思相同

dimensions = (200, 50)
# 虽然元组无法更改，但是可以给元组变量重新赋值
dimensions = (50, 200)

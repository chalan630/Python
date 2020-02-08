'''
@Description: 
@Author: chalan630
@Date: 2019-12-25 14:23:08
@LastEditTime : 2020-02-08 15:21:53
'''
# 集合
{'e', 'b', 'g'}                 # 创建集合
a = set('abacad')
b = set('adcged')
c = set()                       # 创建空集合
d = {}                          # 创建空字典
a - b
# output: {'b'}
a | b                     # a or b
# output: {'g', 'c', 'd', 'e', 'b', 'a'}
a & b
# output: {'d', 'a', 'c'}
a ^ b
# output: {'e', 'b', 'g'}

# 字典
alien_0 = {'color': 'green', 'points': 5}
dict([('sape', 4139), ('guido', 4127)])

# 访问键值对
alien_0['color']

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# 修改键值对
alien_0['color'] = 'red'

# 删除键值对
del alien_0['points']

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# 遍历键值对
for key, value in user_0.items():
    print("\nKey:" + key)
    print("Value" + value)

# 遍历字典中的所有键
for key in user_0.keys():
    print(key, end=' ')

# 按顺序遍历字典中的所有键
for key in sorted(user_0.keys()):
    print(key, end=' ')

# 遍历字典中的所有值
for value in user_0.values():
    print(value, end=' ')

# 字典中的值可能出现重复的情况
for value in set(user_0.values()):                         # set()集合，去除列表中重复元素
    print(value, end=' ')

# 字典列表
alien_1 = {'color': 'yellow', 'points': 4}
alien_2 = {'color': 'red', 'points': 7}
aliens = [alien_0, alien_1, alien_2]

# 批量生成字典列表
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 批量修改
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speen'] = 'medium'
        alien['points'] = 10
    else:
        alien['color'] = 'red'
        alien['speen'] = 'fast'
        alien['points'] = 20

# 字典中存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

# 字典中嵌套字典
users = {
    'make': {
        'first': 'albert',
        'last': 'einstein',
    },
    'jake': {
        'first': 'marie',
        'last': 'curie',
    },
}

# 内置函数
len(dict)                       # 计算字典元素个数，即键的总数。

# 内置方法
dict.clear()                    # 删除字典内所有元素
dict.copy()                     # 返回一个字典的浅复制
dict.get(key, default=None)     # 返回指定键的值，如果值不在字典中返回default值
dict.items()                    # 以列表返回可遍历的(键, 值) 元组数组
dict.keys()                     # 以列表返回一个字典所有的键

'''
@Description: Iterator & Generator
@Author: chalan630
@Date: 2019-12-27 11:12:05
@LastEditTime : 2019-12-28 19:56:52
'''

# 迭代器(Iterator)
# 可以记住遍历的位置和对象
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

list1 = [1,2,3,4,5,6,7,8]
it = iter(list1)
print(next(it))
# output:1
print(next(it))
# output:2
for x in it:
    print(x, end=' ')
# output:3 4 5 6 7 8
print('\n')

# 创建迭代器
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for i in range(0, 5):
    print(next(myiter))

'''
output:
1
3
5
7
9
'''

# 生成器
# 列表元素可由公式推算出来 换句话:已知通项公式，获得下一项
# 生成器是一种特殊的迭代器
i = (x * x for x in range(10))
# 表达式与列表生成式类似

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# 生成器完成的操作同样可以用迭代器完成
# 生成器写法更为紧凑，会自动创建__iter__和__next__方法

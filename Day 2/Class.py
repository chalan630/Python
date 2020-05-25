'''
@Description: Class.py
@Author: chalan630
@Date: 2019-12-25 14:23:08
@LastEditTime: 2020-05-20 01:01:42
'''
# 创建类

    # xx: 公有变量
    # _xx: 私有属性或方法，类对象和子类可以访问 import禁止导入
    # __xx: 私有属性或方法，无法在外部直接访问
    # __xx__: 系统定义名字
    # xx_: 避免与关键字冲突

class Dog():
    # 定义基本类型
    name = ''
    age = 0
    # 私有属性或方法，无法在外部直接访问
    __weight = 0
    # 定义构造方法
    def __init__(self, name, age, weight):              # self代表类的实例，代表当前对象的地址
        """初始化属性name和age"""
        self.name = name
        self.age = age
        self.__weight

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")

    def update_age(self):
        self.age += 1

    def get_weight(self):
        print(self.__weight)


my_dog = Dog('willie', 6, 50)       # 实例化
my_dog.name                         # 访问属性
my_dog.sit()                        # 调用方法
# 修改属性的值
my_dog.age = 7                      # 直接修改属性值
my_dog.update_age()                 # 通过方法修改属性值

class Husky(Dog):
    iq = 0
    def __init__(self, name, age, weight, iq):
        self.name = name
        self.age = age
        self.__weight = weight
        self.ip = iq
    def get_iq(self):
        print(self.iq)


'''
类的专有方法:
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __truediv__: 除运算
    __mod__: 求余运算
    __pow__: 乘方
'''

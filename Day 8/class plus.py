'''
@Descripttion: 
@version: 
@Author: chalan630
@Date: 2020-05-20 01:02:49
@LastEditTime: 2020-05-20 01:39:35
'''


class A:
    class_var = '类变量'                    # 类变量，类定义内部定义的变量（可以认为类内部没有self开头定义的变量是类变量）

    def __init__(self):
        self.instance_var = '成员变量'      # 实例变量，类定义内部__init__函数内以self开头定义的变量

    def normalMethod(self):                # 实例方法，隐含参数为类实例self
        try:
            print(self.class_var)
        except NameError:
            print("无法访问类变量")
        try:
            print(self.instance_var)
        except NameError:
            print("无法访问实例变量")

    @classmethod
    def classMethod(cls):                  # 类方法，隐含参数为类本身
        try:
            print(cls.class_var)
        except NameError:
            print("无法访问类变量")
        try:
            print(cls.instance_var)
        except NameError:
            print("无法访问实例变量")

    @staticmethod
    def staticMethod():                    # 静态方法，无隐含参数
        print(A.class_var)

    @staticmethod
    def aFactory(step):                    # 简单工厂模式样例
        if step == 1:
            return A()
        else:
            print('error!')


a = A()
a.normalMethod()            # 成功
A.normalMethod()            # 报错

"""
实例方法：
    1. 只能由实例调用
    2. 可以访问类变量与成员变量
    3. 对于任意的类，每进行一次实例化，就会产生一个实例方法，需要消耗内存
"""

a.classMethod()             # 成功
A.classMethod()             # 成功
"""
类方法：
    1. 可以由类调用，而且因为传入了参数cls，故也可以由实例来调用
    2. 只能访问类变量，无法访问成员变量
"""

a.staticMethod()            # 成功
A.staticMethod()            # 成功
"""
静态方法：
    1. 可以由实例与类调用
    2. 只能通过类名访问类变量
    3. 不用实例化就可以调用，多用于工厂模式
"""
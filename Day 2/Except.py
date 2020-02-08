'''
@Description: 异常处理
@Author: chalan630
@Date: 2019-12-25 14:23:08
@LastEditTime : 2020-02-08 15:22:15
'''
# 使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("Error!")

# 使用异常处理避免崩溃
try:
    """可能出现异常的代码块"""
    pass
except BaseException:
    """发生异常后的做法"""
    pass
else:
    """异常代码正常执行时运行的代码"""
    pass
finally:
    """不管有没有异常都会执行的代码"""

# 抛出异常
# Python使用raise语句抛出一个指定的异常

# 用户自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

# 在没完善一个程序之前，我们不知道程序在哪里会出错，
# 与其让它在运行最崩溃，不如在出现错误条件时就崩溃，
# 这时候就需要assert断言的帮助

assert 1 == 1           # True 继续运行
assert 1 == 0           # False 程序中断抛出AssertionError

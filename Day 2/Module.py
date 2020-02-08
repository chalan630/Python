'''
@Description: 
@Author: chalan630
@Date: 2019-12-25 14:23:08
@LastEditTime : 2020-02-08 15:22:26
'''
# 模块定义
# pizza.py
# def make_pizza(size, *toppings):
#     print("\nMaking a " + str(size) + 
#         "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
# making_pizzaes.py
import pizza                            # 导入模块

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza            # 导入特定的函数

from pizza import make_pizza as mp      # 使用as给函数指定别名
import pizza as p                       # 使用as给模块指定别名
from pizza import *                     # 导入模块中的所有函数

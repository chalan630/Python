'''
@Descripttion: 全局变量
@version: 0.4
@Author: chalan630
@Date: 2020-03-03 19:21:58
@LastEditTime: 2020-03-17 21:06:37
'''
"""
全局变量
isGameStart
isHeroLoad
"""

def _init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue
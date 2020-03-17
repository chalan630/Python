"""
全局变量
isGameStatus 0游戏启动过程 1按下启动按钮
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
'''
@Descripttion: 
@version: ver0.6
@Author: chalan630
@Date: 2020-03-21 21:44:12
@LastEditTime: 2020-03-24 23:01:47
'''
"""
全局变量
isGameStatus 'start','menu','sign_in','select_hero','game_map_select','game_start','board','bgm'
isSelectHero
isHeroLoad
isPause
hero_name
username
hero
score
rocks
password_text_box
username_text_box
again_text_box
error_type  # 登录注册中的错误信息
load_map    # 加载地图
level       # 级别
backStatus  # ranking list专用
"""


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, def_value=None):
    try:
        return _global_dict[name]
    except KeyError:
        return def_value

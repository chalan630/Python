import gameFlag as gl
import pygame
import sys
from config import Config
import gameFunction as gf
from textbox import TextBox


def btn_start():
    """
    开始按钮按下时触发函数(二级函数)
    :return:
    """
    print("我被按下了")
    gl.set_value('isGameStatus', 'game_map_select')


def btn_quit():
    """
    退出按钮按下时触发函数(二级函数)
    :return:
    """
    print('See you next time!')
    sys.exit()


def btn_pause():
    """
    切换暂停状态(三级函数)
    :return:
    """
    if gl.get_value('isPause'):
        gl.set_value('isPause', False)
    else:
        gl.set_value('isPause', True)


def btn_endless_mode():
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('GameMode', 'endless')


def btn_map1():
    gl.set_value('load_map', 1)
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('GameMode', 'normal')


def btn_map2():
    gl.set_value('load_map', 2)
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('GameMode', 'endless')


def btn_map3():
    gl.set_value('load_map', 3)
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('GameMode', 'endless')


def btn_restart():
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('isLoadHero', False)
    gl.set_value('level', 1)
    print("再来一次")


def btn_log_out():
    gl.set_value('isGameStatus', 'start')


def btn_sign_in():
    gl.set_value('isGameStatus', 'sign_in')
    font = pygame.font.Font(Config.get('fontfolder') + 'pf.ttf', 36)
    name_text_box = gf.TextBox(250, 50, 112, 300, font, callback=gf.callback)
    pass_text_box = TextBox(250, 50, 112, 400, font, callback=gf.callback)
    gl.set_value('name_text_box', name_text_box)
    gl.set_value('pass_text_box', pass_text_box)
    print('sign_in')


def btn_sign_in_check():
    pass_text_box = gl.get_value('pass_text_box')
    name_text_box = gl.get_value('name_text_box')
    password = pass_text_box.get_text()
    username = name_text_box.get_text()
    with open('user.txt', 'r') as f:
        r_username, r_password = f.readline().split('/')
    if r_username == username and r_password == password:
        gl.set_value('error_type', 0)
        gl.set_value('isGameStatus', 'menu')
    else:
        gl.set_value('error_type', 1)
        pass_text_box.clean_text()
        name_text_box.clean_text()


def btn_register():
    print('register')
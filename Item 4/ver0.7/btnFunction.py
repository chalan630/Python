import gameFlag as gl
import pygame
import sys
from config import Config
import gameFunction as gf
from textbox import TextBox
import pymysql
import hashlib


pygame.mixer.init()
click_sound = pygame.mixer.Sound(Config.get('musicfolder') + "click.wav")
click_sound.set_volume(0.2)


def btn_start():
    """
    开始按钮按下时触发函数(二级函数)
    :return:
    """
    print("我被按下了")
    click_sound.play()
    gl.set_value('isGameStatus', 'game_map_select')


def btn_quit():
    """
    退出按钮按下时触发函数(二级函数)
    :return:
    """
    print('See you next time!')
    click_sound.play()
    sys.exit()


def btn_pause():
    """
    切换暂停状态(三级函数)
    :return:
    """
    click_sound.play()
    if gl.get_value('isPause'):
        gl.set_value('isPause', False)
    else:
        gl.set_value('isPause', True)


def btn_endless_mode():
    click_sound.play()
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('GameMode', 'endless')
    gl.set_value('load_map', 0)


def btn_map1():
    click_sound.play()
    gl.set_value('load_map', 1)
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('GameMode', 'normal')


def btn_map2():
    click_sound.play()
    gl.set_value('load_map', 2)
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('GameMode', 'normal')


def btn_map3():
    click_sound.play()
    gl.set_value('load_map', 3)
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('GameMode', 'normal')


def btn_tom():
    print('you select tom!')
    click_sound.play()
    gl.set_value('hero_name', 'tom')
    gl.set_value('isSelectHero', True)
    gl.set_value('isGameStatus', 'game_start')


def btn_jerry():
    print('you select jerry!')
    click_sound.play()
    gl.set_value('hero_name', 'jerry')
    gl.set_value('isSelectHero', True)
    gl.set_value('isGameStatus', 'game_start')


def btn_restart():
    click_sound.play()
    gl.set_value('isGameStatus', 'game_start')
    gl.set_value('isLoadHero', False)
    gl.set_value('level', 1)
    print("再来一次")


def btn_log_out():
    click_sound.play()
    gl.set_value('isGameStatus', 'start')


def btn_sound():
    click_sound.play()
    if gl.get_value('bgm'):
        gl.set_value('bgm', False)
    else:
        gl.set_value('bgm', True)
    print(gl.get_value('bgm'));


def btn_sign_in():
    click_sound.play()
    gl.set_value('isGameStatus', 'sign_in')
    gl.set_value('error_type', 0)
    font = pygame.font.Font(Config.get('fontfolder') + 'pf.ttf', 36)
    name_text_box = TextBox(250, 50, 112, 300, font, callback=gf.callback)
    pass_text_box = TextBox(250, 50, 112, 400, font, callback=gf.callback)
    gl.set_value('name_text_box', name_text_box)
    gl.set_value('pass_text_box', pass_text_box)
    print('sign_in')


def btn_rank():
    click_sound.play()
    gl.set_value('backStatus', gl.get_value('isGameStatus'))
    gl.set_value('isGameStatus', 'board')


def btn_back():
    click_sound.play()
    key_word = gl.get_value('isGameStatus')
    gl.set_value('isLoadHero', False)
    gl.set_value('isSelectHero', False)
    if key_word == 'board':
        print(gl.get_value('backStatus'))
        gl.set_value('isGameStatus', gl.get_value('backStatus'))
    elif key_word == 'menu' or key_word == 'sign_in' or key_word == 'register':
        gl.set_value('isGameStatus', 'start')
    elif key_word == 'game_map_select' or \
            key_word == 'select_hero' or \
            key_word == 'game_start' or \
            key_word == 'game_over':
        gl.set_value('isGameStatus', 'menu')
        gl.set_value('isLoadHero', False)
        gl.set_value('isPause', False)
        gl.set_value('load_map', 0)


def btn_sign_in_check():
    click_sound.play()
    pass_text_box = gl.get_value('pass_text_box')
    name_text_box = gl.get_value('name_text_box')
    password = pass_text_box.get_text()
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    username = name_text_box.get_text()
    db = pymysql.connect("localhost", "root", "19971231", "hider")
    cursor = db.cursor()
    sql = "SELECT * from user where nickname='%s' and passwd='%s'" % (username, password)
    cursor.execute(sql)
    if cursor.fetchone():
        gl.set_value('error_type', 0)
        gl.set_value('isGameStatus', 'menu')
        gl.set_value('username', username)
    else:
        gl.set_value('error_type', 1)
        pass_text_box.clean_text()
        name_text_box.clean_text()


def btn_register():
    click_sound.play()
    gl.set_value('isGameStatus', 'register')
    gl.set_value('error_type', 0)
    font = pygame.font.Font(Config.get('fontfolder') + 'pf.ttf', 36)
    name_text_box = TextBox(250, 50, 112, 260, font, callback=gf.callback)
    pass_text_box = TextBox(250, 50, 112, 360, font, callback=gf.callback)
    again_text_box = TextBox(250, 50, 112, 460, font, callback=gf.callback)
    gl.set_value('name_text_box', name_text_box)
    gl.set_value('pass_text_box', pass_text_box)
    gl.set_value('again_text_box', again_text_box)
    print('register')


def btn_register_check():
    click_sound.play()
    db = pymysql.connect("localhost", "root", "19971231", "hider")
    cursor = db.cursor()
    name_text_box = gl.get_value('name_text_box')
    pass_text_box = gl.get_value('pass_text_box')
    again_text_box = gl.get_value('again_text_box')
    password = pass_text_box.get_text()
    username = name_text_box.get_text()
    again = again_text_box.get_text()
    if len(username) != 0 and len(password) != 0:
        if password == again:
            sql = "SELECT * from user where nickname='%s'" % username
            cursor.execute(sql)
            data = cursor.fetchone()
            if data:
                print('用户名已存在')
                gl.set_value('error_type', 2)
            else:
                sql = "INSERT INTO USER(passwd, nickname) VALUES('%s', '%s')"\
                    % (hashlib.md5(password.encode('utf-8')).hexdigest(), username)
                cursor.execute(sql)
                print('注册成功')
                gl.set_value('isGameStatus', 'start')
        else:
            gl.set_value('error_type', 4)
            pass_text_box.clean_text()
            name_text_box.clean_text()
            again_text_box.clean_text()
    else:
        gl.set_value('error_type', 3)

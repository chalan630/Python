'''
@Descripttion: 游戏函数
@version: ver0.3
@Author: chalan630
@Date: 2020-03-02 23:37:29
@LastEditTime: 2020-03-03 16:32:13
'''
import pygame
import sys
import gameFlag as gl
from hero import Hero
from config import Config


def check_keydown_events(event):
    hero = gl.get_value('hero')
    if event.key == pygame.K_RIGHT:
        hero.setDirect('right', True)
    elif event.key == pygame.K_LEFT:
        hero.setDirect('left', True)
    elif event.key == pygame.K_UP:
        hero.setDirect('up', True)
    elif event.key == pygame.K_DOWN:
        hero.setDirect('down', True)
    elif event.key == pygame.K_q:
        gl.set_value('isGameStart', False)


def check_keyup_events(event):
    hero = gl.get_value('hero')
    if event.key == pygame.K_RIGHT:
        hero.setDirect('right', False)
    elif event.key == pygame.K_LEFT:
        hero.setDirect('left', False)
    elif event.key == pygame.K_UP:
        hero.setDirect('up', False)
    elif event.key == pygame.K_DOWN:
        hero.setDirect('down', False)


def check_event(Btns):
    """
    游戏事件检查
    :param Btns: 按键字典
    :return:
    """
    # 获取鼠标坐标
    mx, my = pygame.mouse.get_pos()
    # 获取键盘输入，并处理事件
    for event in pygame.event.get():  # 事件循环
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)
        elif event.type == pygame.MOUSEMOTION:
            # 判断鼠标是否移动到按钮范围之内
            for btn in Btns.values():
                btn.getFocus(mx, my)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                for btn in Btns.values():
                    btn.mouseDown(mx, my)
        elif event.type == pygame.MOUSEBUTTONUP:
            for btn in Btns.values():
                btn.mouseUp()
        # elif event.type == pygame.K_DOWN:
        #     if event.key == pygame.K_q:
        #         gl.set_value('isGameStart', False)

#
def btn_start():
    print("我被按下了")
    gl.set_value('isGameStart', True)

def btn_quit():
    print('See you next time!')
    sys.exit()


def game_start(screen):
    """
    游戏开始函数
    :param screen: 获得游戏屏幕数据
    """
    if not gl.get_value('isLoadHero'):
        hero = Hero('hero', Config.get('imgfolder'), screen)
        gl.set_value('hero', hero)
        gl.set_value('isLoadHero', True)
    else:
        hero = gl.get_value('hero')
        hero.blitMe()


def draw_button(screen, Btns):
    if not gl.get_value('isGameStart'):
        Btns['start'].draw(screen)
        Btns['quit'].draw(screen)
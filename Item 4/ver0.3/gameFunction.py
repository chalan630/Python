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

# TODO: 2. 不能连续触发
def check_keydown_events():
    hero = gl.get_value('hero')
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
        hero.moveUp()
    if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
        hero.moveDown()
    if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        hero.moveLeft()
    if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        hero.moveRight()

def check_event(Btns):
    # 获取鼠标坐标
    mx, my = pygame.mouse.get_pos()
    # 获取键盘输入，并处理事件
    for event in pygame.event.get():  # 事件循环
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events()
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

def btn_start():
    print("我被按下了")
    gl.set_value('isGameStart', True)

def btn_quit():
    print('See you next time!')
    sys.exit()

def game_start(screen):
    if not gl.get_value('isLoadHero'):
        hero = Hero('hero', Config.get('imgfolder'), screen)
        gl.set_value('hero', hero)
        gl.set_value('isLoadHero', True)
    else:
        hero = gl.get_value('hero')
        screen.blit(hero.image1, hero.rect)


def draw_button(screen, Btns):
    if not gl.get_value('isGameStart'):
        Btns['start'].draw(screen)
        Btns['quit'].draw(screen)
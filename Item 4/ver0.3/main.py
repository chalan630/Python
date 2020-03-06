'''
@Descripttion: 主函数
@version: 0.3
@Author: chalan630
@Date: 2020-02-28 16:26:24
@LastEditTime: 2020-03-03 16:20:59
'''

import pygame
import os, sys
# 自定义部分
import gameFunction as gf
import gameFlag as gl
from config import Config
from background import Background
from button import Button

def main():

    # 程序中用到的常量
    gl._init()
    gl.set_value('isGameStart', False)
    gl.set_value('isLoadHero', False)

    # 改变目录 修正 vscode 中的路径异常问题
    os.chdir(sys.path[0])

    # 初始化响应环境
    pygame.init()
    pygame.display.set_caption('躲避者 Demo Ver0.2')
    screen = pygame.display.set_mode([Config.get('WIDTH'), Config.get('HEIGHT')])
    # 实例化Pygame 的time 模块的 Clock 对象
    clock = pygame.time.Clock()
    # 初始化图片
    # TODO: 1. 将按钮操作移出main.py，保证main.py简洁清晰，尝试使用精灵类解决

    bg = Background(screen, Config.get('imgfolder'), 'background.png')
    # 开始按钮图片
    startBtns = {}
    startBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'button_start_0.png')
    startBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'button_start_1.png')
    startBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'button_start_2.png')
    quitBtns = {}
    quitBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'button_quit_0.png')
    quitBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'button_quit_1.png')
    quitBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'button_quit_2.png')
    # 初始化按钮字体
    btnFont = pygame.font.SysFont(Config.get('fontfolder') + 'pf.ttf', 40)
    # 初始化按钮
    # 开始按钮
    Btns = {}
    Btns['start'] = Button(90, 200, "", startBtns['Normal'], startBtns['Select'], \
                           startBtns['Click'], gf.btn_start, btnFont)
    Btns['quit'] = Button(90, 400, "", quitBtns['Normal'], quitBtns['Select'], quitBtns['Click'], gf.btn_quit, btnFont)

    while True:
        gf.check_event(Btns)
        bg.action()
        bg.draw()
        gf.draw_button(screen, Btns)
        if gl.get_value('isGameStart'):
            gf.game_start(screen)
        pygame.display.update()
        # 设置帧率
        clock.tick(60)


if __name__ == "__main__":
    main()

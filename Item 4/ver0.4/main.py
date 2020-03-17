'''
@Descripttion: 主函数
@version: 0.4
@Author: chalan630
@Date: 2020-02-28 16:26:24
@LastEditTime: 2020-03-03 16:20:59
'''

"""
编程规范：
    函数名使用下划线分割
    类方法使用小驼峰
    常量全大写
"""

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
    gl.set_value('isGameStatus', 0)
    gl.set_value('isPause', False)
    gl.set_value('isLoadHero', False)

    # 改变目录 修正 vscode 中的路径异常问题
    os.chdir(sys.path[0])

    # 初始化响应环境
    pygame.init()
    pygame.display.set_caption('躲避者 Demo Ver0.4')
    screen = pygame.display.set_mode([Config.get('WIDTH'), Config.get('HEIGHT')])
    # 实例化Pygame 的time 模块的 Clock 对象
    clock = pygame.time.Clock()
    # 初始化图片

    bg = Background(screen, Config.get('imgfolder'), 'background.png')
    # 开始按钮图片
    startBtns = {}
    startBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'button_start_0.png').convert_alpha()
    startBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'button_start_1.png').convert_alpha()
    startBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'button_start_2.png').convert_alpha()
    quitBtns = {}
    quitBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'button_quit_0.png').convert_alpha()
    quitBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'button_quit_1.png').convert_alpha()
    quitBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'button_quit_2.png').convert_alpha()
    pauseBtns = {}
    pauseBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'pause_0.png').convert_alpha()
    pauseBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'pause_1.png').convert_alpha()
    pauseBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'pause_2.png').convert_alpha()
    resumeBtns = {}
    resumeBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'resume_0.png').convert_alpha()
    resumeBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'resume_1.png').convert_alpha()
    resumeBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'resume_2.png').convert_alpha()
    restartBtns = {}
    restartBtns['Normal'] = pygame.image.load(Config.get('imgfolder') + 'button_restart_0.png').convert_alpha()
    restartBtns['Select'] = pygame.image.load(Config.get('imgfolder') + 'button_restart_1.png').convert_alpha()
    restartBtns['Click'] = pygame.image.load(Config.get('imgfolder') + 'button_restart_2.png').convert_alpha()

    pause_rect = pauseBtns['Normal'].get_rect()
    pause_rect.left, pause_rect.top = Config.get('WIDTH') - pause_rect.width - 10, 10
    # 初始化按钮字体
    btnFont = pygame.font.SysFont(Config.get('fontfolder') + 'pf.ttf', 40)
    # 初始化按钮
    # 开始按钮
    Btns = {}
    Btns['start'] = Button(90, 200, "", startBtns['Normal'], startBtns['Select'], \
                           startBtns['Click'], gf.btn_start, btnFont)
    Btns['quit'] = Button(90, 400, "", quitBtns['Normal'], quitBtns['Select'], \
                          quitBtns['Click'], gf.btn_quit, btnFont)
    Btns['pause'] = Button(pause_rect.left, pause_rect.top, "", pauseBtns['Normal'], \
                           pauseBtns['Select'], pauseBtns['Click'], gf.btn_pause, btnFont)
    Btns['restart'] = Button(90, 400, "again", restartBtns['Normal'], restartBtns['Select'], \
                             restartBtns['Click'], gf.btn_restart, btnFont)

    # 游戏正文
    while True:
        gf.check_event(Btns)    # 获取鼠标键盘事件
        # bg.action()             # 背景运动
        bg.draw(not gl.get_value('isPause'))               # 背景描绘
        gf.draw_button(screen, Btns)  # 按钮绘制
        if gl.get_value('isGameStatus') != 0:
            if gl.get_value('isGameStatus') == 1:
                gf.game_start(screen, Btns)
            if gl.get_value('isGameStatus') == -1:
                gf.game_over(screen)

        pygame.display.update()
        # 设置帧率
        clock.tick(60)


if __name__ == "__main__":
    main()

'''
@Descripttion: 
@version: 0.2
@Author: chalan630
@Date: 2020-02-28 16:26:24
@LastEditTime: 2020-02-29 19:23:01
'''

import pygame
import os, sys
# 自定义部分
from config import Config
from background import Background
from button import Button
import gameFunction as gf

def main():
    os.chdir(sys.path[0])

    pygame.init()
    pygame.display.set_caption('躲避者 Demo Ver0.2')
    screen = pygame.display.set_mode([Config.get('WIDTH'), Config.get('HEIGHT')])
    # 实例化Pygame 的time 模块的 Clock 对象
    clock = pygame.time.Clock()
    # 初始化图片
    bg = Background(screen, Config.get('imgfolder'), 'background.png')
    startBtnNormal = pygame.image.load(Config.get('imgfolder') + 'button_start_0.png')
    startBtnSelect = pygame.image.load(Config.get('imgfolder') + 'button_start_1.png')
    startBtnClick = pygame.image.load(Config.get('imgfolder') + 'button_start_2.png')
    # 初始化字体按钮
    btnFont = pygame.font.SysFont(Config.get('fontfolder') + 'pf.ttf', 40)
    # 初始化按钮
    btn = Button(90, 200, "", startBtnNormal, startBtnSelect, startBtnClick, gf.btn_call_back, btnFont)

    while True:
        gf.check_event(btn)
        bg.action()
        bg.draw()
        btn.draw(screen)
        pygame.display.update()
        # 设置帧率
        clock.tick(60)
    

if __name__ == "__main__":
    main()

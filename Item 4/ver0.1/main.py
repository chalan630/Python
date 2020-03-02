'''
@Descripttion: 
@version: 0.1
@Author: chalan630
@Date: 2020-02-28 16:26:24
@LastEditTime: 2020-02-29 19:23:01
'''

import pygame
import os, sys
# 自定义部分
from config import Config
from background import Background
import gameFunction as gf

def main():
    os.chdir(sys.path[0])

    pygame.init()
    pygame.display.set_caption('躲避者 Demo Ver0.1')
    screen = pygame.display.set_mode([Config.get('WIDTH'), Config.get('HEIGHT')])
    # 实例化Pygame 的time 模块的 Clock 对象
    clock = pygame.time.Clock()
    # 初始化背景
    bg = Background(screen, Config.get('imgfolder'))
    while True:
        gf.check_event()
        bg.action()
        bg.draw()
        pygame.display.update()
        # 设置帧率
        clock.tick(60)
    


if __name__ == "__main__":
    main()

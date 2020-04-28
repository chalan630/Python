'''
@Descripttion: 主函数
@version: ver0.6
@Author: chalan630
@Date: 2020-02-28 16:26:24
@LastEditTime: 2020-03-23 15:09:30
'''
import pygame
import os, sys
# 自定义部分
import gameFunction as gf
import gameFlag as gl
import button_item
from config import Config
from background import Background

"""
编程规范：
    函数名使用下划线分割
    类方法使用小驼峰
    常量全大写
"""

def main():

    # 程序中用到的常量
    gl._init()
    # gl.set_value('isGameStatus', 'start')
    gl.set_value('GameMode', 'endless')
    gl.set_value('isGameStatus', 'menu')
    gl.set_value('isPause', False)
    gl.set_value('isLoadHero', False)
    gl.set_value('error_type', 0)
    gl.set_value('load_map', 0)

    # 改变目录 修正 vscode 中的路径异常问题
    os.chdir(sys.path[0])

    # 初始化响应环境
    pygame.init()
    pygame.display.set_caption('躲避者 Demo Ver0.6')
    screen = pygame.display.set_mode([Config.get('WIDTH'), Config.get('HEIGHT')])
    # 实例化Pygame 的time 模块的 Clock 对象
    clock = pygame.time.Clock()
    # 初始化图片
    # 垂直竖版风格手游地图打包下载-合集成套素材
    # 使用数组，保存所有背景
    bg = [Background(screen, Config.get('imgfolder'), 'background0.png'),\
          Background(screen, Config.get('imgfolder'), 'background1.png'),\
          Background(screen, Config.get('imgfolder'), 'background2.png'),\
          Background(screen, Config.get('imgfolder'), 'background3.png')]
    Btns = button_item.init_button()       # 将按钮初始化封装为函数

    title_font = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 72)
    game_title_text = title_font.render("躲  避  者", True, (255, 255, 255))

    # 游戏正文
    while True:
        gf.check_event(Btns)    # 获取鼠标键盘事件
        # bg.action()             # 背景运动
        bg[gl.get_value('load_map')].draw(not gl.get_value('isPause'))               # 背景描绘
        if gl.get_value('isGameStatus') != 0:
            if gl.get_value('isGameStatus') == 'start':
                screen.blit(game_title_text, (100, 150))
            if gl.get_value('isGameStatus') == 'sign_in':
                gf.sign_in(screen)
            if gl.get_value('isGameStatus') == 'game_start':
                gf.game_start(screen)
            if gl.get_value('isGameStatus') == 'game_over':
                gf.game_over(screen)
        gf.draw_button(screen, Btns)  # 按钮绘制
        gf.error_message(screen)
        pygame.display.update()
        # 设置帧率
        clock.tick(60)


if __name__ == "__main__":
    main()

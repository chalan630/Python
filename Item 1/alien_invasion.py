'''
@Description: 主文件
@Author: chalan630
@Date: 2020-01-13 23:04:51
@LastEditTime : 2020-02-08 17:01:44
'''

import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景设置
    ai_settings = Settings()
    # 创建显示窗口 返回一个surface
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建 Play 按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:  # 游戏循环
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()

'''
@Descripttion: 飞船外形
@Author: chalan630
@Date: 2020-01-14 22:06:08
@LastEditTime : 2020-01-15 21:22:56
'''
import pygame
import os
import sys


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        os.chdir(sys.path[0])
        self.image = pygame.image.load('images/ship.bmp')       # 返回一个surface
        self.rect = self.image.get_rect()                       # 获取相应surface的属性rect
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx            # center、centerx、centery
        self.rect.bottom = self.screen_rect.bottom              # top、bottom、left、right
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)                  # rect.centrx中只能保存整数
        self.bot = float(self.rect.bottom)  # test
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False              # test
        self.moving_down = False            # test

    def update(self):
        # 以速度为单位，向四个方向移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bot -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bot += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.bot

    def blitme(self):               # 绘制
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


'''
@Descripttion: 敌人类
@version: ver0.6
@Author: chalan630
@Date: 2020-03-10 16:26:24
@LastEditTime: 2020-03-23 15:08:54
'''

import pygame
import random
from config import Config


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyName, imagePath, screen, damage, level=1):
        """
        创建通用enemy类
        :param enemyName: {str}输入敌人图片文件名
        :param imagePath: {str}图片路径
        :param screen: {object}屏幕数据
        :param score: {int}该类型敌人的分值
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath + enemyName + '.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.speed = [0, 0]     # 竖直方向, 水平方向
        self.rect.left, self.rect.top = [random.randint(0, self.width - self.rect.width), \
                                         random.randint(-2 * self.height, 0)]
        self.mask = pygame.mask.from_surface(self.image)  # 用于碰撞检测
        self.score = Config.get('score')
        self.damage = damage
        self.reset_status(level)
        self.isCollide = False

    def reset_status(self, level):
        speed_list = [-1, 0, 1]
        flag = random.randint(0, 2)
        self.speed[0] = 2 + (level - 1) * 0.1
        self.speed[1] = speed_list[flag]
        self.score = self.score * level
        self.damage += self.damage * (level - 1) * 0.1

    def moveRAL(self):
        """
        敌方左右移动
        :return:
        """
        if self.speed[1] > 0:   # 右
            if self.rect.right < self.width:
                if self.rect.left + self.speed[1] > self.width:
                    self.rect.left = self.width
                else:
                    self.rect.left += self.speed[1]
            elif self.rect.right == self.width:
                self.speed[1] = -self.speed[1]
        elif self.speed[1] < 0:
            if self.rect.left > 0:
                if self.rect.left + self.speed[1] < 0:
                    self.rect.left = 0
                else:
                    self.rect.left += self.speed[1]
            elif self.rect.left == 0:
                self.speed[1] = -self.speed[1]

    def move(self):
        if self.height > self.rect.top:
            self.rect.top += self.speed[0]
            if self.rect.left >= 0 and self.rect.right <= self.width:
                self.moveRAL()
        if self.rect.top < -720:       # 防止石块永不落下，无法更新石块精灵组
            self.speed[0] = 2

    def blitMe(self, flag):               # 绘制
        if flag:
            self.move()
        self.screen.blit(self.image, self.rect)


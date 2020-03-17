'''
@Descripttion: 敌人类
@version: 0.4
@Author: chalan630
@Date: 2020-03-10 16:26:24
@LastEditTime: 2020-03-03 16:20:59
'''

import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyName, imagePath, screen, score):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath + enemyName + '.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.speed = [2, 1]
        self.rect.left, self.rect.top = random.randint(0, self.width-self.rect.width),\
                                        random.randint(-5 * self.height, 0)         #在页面外部上5个高度范围内随机生成
        self.mask = pygame.mask.from_surface(self.image)  # 用于碰撞检测
        self.direct = [0, 0, 0, 0]
        self.initDirect()   # 初始化方向
        self.score = score

    def initDirect(self):
        self.direct[1] = 1
        flag = random.randint(0, 2)
        if flag == 1:
            self.direct[2] = 1
        elif flag == 2:
            self.direct[3] = 1

    def moveRAL(self):
        """
        敌方左右移动
        :return:
        """
        if self.direct[2] == 1:
            if self.rect.left > 0:
                self.rect.left -= self.speed[1]
            else:
                self.direct[2] = 0
                self.direct[3] = 1
        elif self.direct[3] == 1:
            if self.rect.right < self.width:
                self.rect.left += self.speed[1]
            else:
                self.direct[3] = 0
                self.direct[2] = 1

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed[0]
            if self.rect.left >= 0 and self.rect.right <= self.width:
                self.moveRAL()

    def blitMe(self, flag):               # 绘制
        if flag:
            self.move()
        self.screen.blit(self.image, self.rect)

    def levelUp(self):
        self.speed[0] = 1.2 * self.speed[0]
        self.speed[1] = 1.1 * self.speed[1]
        self.score = 2 * self.score

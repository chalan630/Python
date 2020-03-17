'''
@Descripttion: 英雄类
@version: ver0.3
@Author: chalan630
@Date: 2020-03-02 23:45:38
@LastEditTime: 2020-03-17 21:05:49
'''
import pygame

class Hero():
    def __init__(self, heroName, imagePath, screen):
        self.image1 = pygame.image.load(imagePath + heroName + '_0.png').convert_alpha()
        self.image2 = pygame.image.load(imagePath + heroName + '_1.png').convert_alpha()
        self.image1 = pygame.transform.scale2x(self.image1)
        self.image2 = pygame.transform.scale2x(self.image2)
        # 用于碰撞检测
        # self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.rect = self.image1.get_rect()
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60  # 减60留给状态栏
        self.speed = 10
        # self.moveFlag = False
        self.direct = [0, 0, 0, 0]

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def blitMe(self):               # 绘制
        """在指定位置绘制飞船"""
        # if self.moveFlag:
        if self.direct[0] == 1:
            self.moveUp()
        if self.direct[1] == 1:
            self.moveDown()
        if self.direct[2] == 1:
            self.moveLeft()
        if self.direct[3] == 1:
            self.moveRight()

        self.screen.blit(self.image1, self.rect)

    # def setMoveFlag(self, attitude=False):
    #     """
    #     设置移动标志
    #     :param attitude: 为True时表示：开始移动
    #     """
    #     self.moveFlag = attitude

    def setDirect(self, str_, attitude=False):
        """
        设置移动方向
        :param str_: 移动方向
        :param attitude: 为True时表示：按下某方向
        """
        key = 0
        value = 0    # 键值
        if attitude:
            value = 1
        elif not attitude:
            value = 0
        if str_ == 'up':
            key = 0
        elif str_ == 'down':
            key = 1
        elif str_ == 'left':
            key = 2
        elif str_ == 'right':
            key = 3
        self.direct[key] = value
        # 防止斜向移动速度过高
        if self.direct.count(1) == 2:
            self.speed = 7
        else:
            self.speed = 10
        # print(self.speed)
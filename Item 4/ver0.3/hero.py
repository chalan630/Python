'''
@Descripttion: 英雄类
@version: ver0.3
@Author: chalan630
@Date: 2020-03-02 23:45:38
@LastEditTime: 2020-03-03 16:32:03
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

'''
@Descripttion: 背动
@version: ver0.5
@Author: chalan630
@Date: 2020-02-29 18:09:53
@LastEditTime: 2020-03-24 23:01:29
'''

import pygame


class Background():
    def __init__(self, screen, imagePath, picName):
        # 场景对象
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 加载图片
        self.image1 = pygame.image.load(imagePath + picName).convert()
        self.image2 = pygame.image.load(imagePath + picName).convert()
        self.image1 = pygame.transform.smoothscale(self.image1, (480, 720))
        self.image2 = pygame.transform.smoothscale(self.image2, (480, 720))
        self.image1_rect = self.image1.get_rect()
        self.image2_rect = self.image2.get_rect()
        # self.screen.size[1]保存的是游戏窗口的高度 rect属性里是有 height参数的
        # 但编辑器不会自动显示，我也是在调试的时候才发现。
        self.y1 = self.screen_rect.height - self.image1_rect.height
        self.y2 = self.y1 - self.image2_rect.height

    # 计算图片绘制坐标
    def action(self, level=1):
        self.y1 = self.y1 + (1 * level)
        self.y2 = self.y2 + (1 * level)
        # 第一张图超出屏幕了，就接到第二张图的后面，以此类推。
        if self.y1 >= self.screen_rect.height:
            self.y1 = self.y2 - self.image1_rect.height
        if self.y2 >= self.screen_rect.height:
            self.y2 = self.y1 - self.image2_rect.height

    def draw(self, flag, level=1):
        """
        绘制地图的两张图片
        :param flag: 游戏是否暂停的标志
        """
        if flag:
            self.action(level)
        self.screen.blit(self.image1, (0, self.y1))
        self.screen.blit(self.image2, (0, self.y2))

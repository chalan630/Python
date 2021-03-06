import pygame
from config import Config


class Star(pygame.sprite.Sprite):
    def __init__(self, name, imagePath, screen, level):
        """
        :param imagePath: {str}图片路径
        :param screen: {object}屏幕数据
        """
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(imagePath + name + '.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.speed = Config.get('speed')  # 竖直方向
        self.mask = pygame.mask.from_surface(self.image)  # 用于碰撞检测
        self.init_speed(level)
        self.score = 0

    def init_speed(self, level):
        if level / 10 > 0:
            self.speed = self.speed + int(level / 10)

    def move(self):
        self.rect.top += self.speed

    def blitMe(self, flag):               # 绘制
        if flag:
            self.move()
        self.screen.blit(self.image, self.rect)

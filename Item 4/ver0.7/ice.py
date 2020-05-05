from star import Star
import pygame
import random


class Ice(Star):
    def __init__(self, name, imagePath, screen, level=1):
        Star.__init__(self, name, imagePath, screen, level)
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect.left, self.rect.top = [random.randint(0, self.width - self.rect.width), \
                                         random.randint(-2 * self.height, 0)]

    def enable(self, hero):
        if not hero.debuff:
            hero.changeDirectFlag = True
            hero.debuff = True

    def disable(self, hero):
        if hero.debuff:
            hero.changeDirectFlag = False
            hero.direct = [0, 0, 0, 0]
            hero.debuff = False

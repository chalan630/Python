from star import Star
import pygame
import random


class Swamp(Star):
    def __init__(self, name, imagePath, screen, level=1):
        Star.__init__(self, name, imagePath, screen, level)
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect.left, self.rect.top = [random.randint(0, self.width - self.rect.width), \
                                         random.randint(-2 * self.height, 0)]
        self.raw_speed = 0

    def enable(self, hero):
        if not hero.debuff:
            self.raw_speed = hero.initSpeed
            hero.debuff = True
        elif hero.debuff:
            hero.speed = int(self.raw_speed / 2)
            hero.initSpeed = int(self.raw_speed / 2)

    def disable(self, hero):
        if hero.debuff:
            hero.initSpeed = self.raw_speed
            hero.speed = self.raw_speed
            hero.debuff = False

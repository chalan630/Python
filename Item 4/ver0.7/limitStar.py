from star import Star
import pygame
import random


class LimitStar(Star):
    def __init__(self, name, imagePath, screen, level=1):
        Star.__init__(self, name, imagePath, screen, level)
        self.image = pygame.transform.smoothscale(self.image, (40, 40))
        self.rect.left, self.rect.top = [random.randint(0, self.width - self.rect.width), \
                                         random.randint(-5 * self.height * (1 + int(level / 10)), \
                                                        -1 * self.height)]
        self.advance_value = 10

    def enable(self, hero, level):
        if hero.HP_now <= hero.HP_upper_limit - self.advance_value:
            hero.HP_now += self.advance_value
        elif hero.HP_upper_limit - self.advance_value < hero.HP_now < hero.HP_upper_limit:
            hero.HP_upper_limit = hero.HP_now + self.advance_value
            hero.HP_now = hero.HP_upper_limit
        elif hero.HP_now == hero.HP_upper_limit:
            hero.HP_upper_limit += self.advance_value
            hero.HP_now = hero.HP_upper_limit



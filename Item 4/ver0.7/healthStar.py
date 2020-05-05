from star import Star
import gameFlag as gl
import random
import pygame


class HealthStar(Star):
    def __init__(self, name, imagePath, screen, level=1):
        Star.__init__(self, name, imagePath, screen, level)
        self.image = pygame.transform.smoothscale(self.image, (40, 40))
        self.rect.left, self.rect.top = [random.randint(0, self.width - self.rect.width), \
                                         random.randint(-3 * self.height * (1 + int(level / 10)), \
                                                        -1 * self.height)]
        self.health_value = 10

    def switch_point(self, level=1):
        return self.health_value * level * 10

    def enable(self, hero, level):
        if hero.HP_now < hero.HP_upper_limit - self.health_value:
            hero.HP_now += self.health_value
        elif hero.HP_upper_limit - self.health_value <= hero.HP_now < hero.HP_upper_limit:
            hero.HP_now = hero.HP_upper_limit
        elif hero.HP_now == hero.HP_upper_limit:
            temp = gl.get_value('score')
            gl.set_value('score', temp + self.switch_point(level))

from star import Star
import gameFlag as gl
import random


class HealthStar(Star):
    def __init__(self, name, imagePath, screen, value, level):
        Star.__init__(self, name, imagePath, screen, level)
        self.rect.left, self.rect.top = [random.randint(0, self.width - self.rect.width), \
                                         random.randint(-1 * self.height, 720)]
        self.health_value = value

    def health(self, hero):
        if hero.HP_now < hero.HP_upper_limit - self.health_value:
            hero.HP_now += self.health_value
        elif hero.HP_upper_limit - self.health_value <= hero.HP_now < hero.HP_upper_limit:
            hero.HP_now = hero.HP_upper_limit
        elif hero.HP_now == hero.HP_upper_limit:
            temp = gl.get_value('score')
            gl.set_value('score', temp + self.switch_point())

    def switch_point(self, level=1):
        return self.health_value * level * 10

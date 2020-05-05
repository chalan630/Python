from star import Star
import random
import pygame
import gameFlag as gl


class ScoreStar(Star):
    def __init__(self, name, imagePath, screen, level=1):
        Star.__init__(self, name, imagePath, screen, level)
        self.image = pygame.transform.smoothscale(self.image, (40, 40))
        self.rect.left, self.rect.top = [random.randint(0, self.width - self.rect.width), \
                                         random.randint(-3 * self.height * (1 + int(level / 10)),\
                                                        -1 * self.height)]
        self.score = 500

    def reset_status(self, level):
        temp_score = self.score + (level - 1) * 100
        return temp_score

    def enable(self, hero, level=1):
        self.reset_status(level)
        gl.set_value('score', gl.get_value('score') + self.score)

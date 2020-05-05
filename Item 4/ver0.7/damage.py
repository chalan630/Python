from star import Star
import pygame
import random


class Damage(Star):
    def __init__(self, name, imagePath, screen, level=1):
        Star.__init__(self, name, imagePath, screen, level)
        self.image = pygame.transform.smoothscale(self.image, (80, 40))
        self.rect.left, self.rect.top = [random.randint(0, self.width - self.rect.width), \
                                         random.randint(-2 * self.height, 0)]
        self.poisoning = pygame.image.load(imagePath + 'poisoning.png').convert_alpha()
        self.poisoning = pygame.transform.smoothscale(self.poisoning, (30, 30))
        self.delay = 30  # 用于延迟

    def enable(self, hero):
        if not hero.debuff:
            hero.debuff = True
        elif hero.debuff and not hero.invincibleFlag:
            if self.delay == 0:
                hero.HP_now -= 10
                self.delay = 30
            else:
                if self.delay % 6:
                    top = hero.rect.top - 40
                    left = hero.rect.left + int(hero.rect.width / 2) - 15
                    self.screen.blit(self.poisoning, (left, top))
                self.delay -= 1

    def disable(self, hero):
        if hero.debuff:
            hero.debuff = False

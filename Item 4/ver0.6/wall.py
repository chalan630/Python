import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, screen, imagePath, position, score):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath + 'grass.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (80, 40))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = position
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.speed = 1
        self.score = score

    def move(self):
        if self.rect.top <= self.height:
            self.rect.top += self.speed

    def blitMe(self, flag):  # 绘制
        if flag:
            self.move()
        self.screen.blit(self.image, self.rect)

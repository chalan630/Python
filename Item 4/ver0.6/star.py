class Star(pygame.sprite.Sprite):
    def __init__(self, imagePath, screen):
        """
        :param imagePath: {str}图片路径
        :param screen: {object}屏幕数据
        :param score: {int}该类型精灵的分值
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath + 'star.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.speed = 0  # 竖直方向
        self.rect.left, self.rect.top = [random.randint(0, self.width - self.rect.width), \
                                         random.randint(0 * self.height, 720)]
        self.mask = pygame.mask.from_surface(self.image)  # 用于碰撞检测
        self.initSpeed()

    def initSpeed(self, level=1):
        self.speed = 2 * level

    def move(self):
        self.rect.top += self.speed

    def blitMe(self, flag):               # 绘制
        if flag:
            self.move()
        self.screen.blit(self.image, self.rect)

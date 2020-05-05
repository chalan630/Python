from hero import Hero


class Jerry(Hero):
    def __init__(self, heroName, imagePath, screen):
        Hero.__init__(self, heroName, imagePath, screen)
        self.gap = 200

    def skill(self):
        self.rect.top -= self.gap
        self.invincibleFlag = True

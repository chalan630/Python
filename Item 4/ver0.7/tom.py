from hero import Hero


class Tom(Hero):
    def __init__(self, heroName, imagePath, screen):
        Hero.__init__(self, heroName, imagePath, screen)
        self.crossFlag = False

    def skill(self):
        self.invincibleFlag = True
        self.crossFlag = True
        self.invincibleTime = 120

    def invincibleStatus(self):
        if self.invincibleFlag:         # 如果处于无敌状态
            if self.invincibleTime == 0:
                self.invincibleFlag = False
                self.invincibleTime = 60
                self.crossFlag = False
            self.invincibleTime -= 1
            self.delay1 -= 1
            if self.delay1 == 5:
                return True
            if self.delay1 == 0:
                self.delay1 = 10
            return False
        else:
            return True

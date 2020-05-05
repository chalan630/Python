'''
@Descripttion: 英雄类
@version: ver0.6
@Author: chalan630
@Date: 2020-03-02 23:45:38
@LastEditTime: 2020-03-23 15:09:19
'''
import pygame
from config import Config
import gameFlag as gl


class Hero:
    def __init__(self, heroName, imagePath, screen):
        # 人物图像
        self.image1 = pygame.image.load(imagePath + heroName + '_0.png').convert_alpha()
        self.image2 = pygame.image.load(imagePath + heroName + '_1.png').convert_alpha()
        self.image1 = pygame.transform.smoothscale(self.image1, (48, 96))
        self.image2 = pygame.transform.smoothscale(self.image2, (48, 96))
        # 技能图标
        self.skill_img = pygame.image.load(imagePath + heroName + '_skill.png').convert_alpha()
        self.skill_img = pygame.transform.smoothscale(self.skill_img, (30, 30))
        # 血条
        self.HP_img = pygame.image.load(Config.get('imgfolder') + 'HP.png').convert_alpha()
        self.HP_img = pygame.transform.smoothscale(self.HP_img, (240, 20))
        self.Font_HP = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 20)
        self.Font_txt = pygame.font.Font(Config.get('fontfolder') + 'button.ttf', 35)
        # 属性
        self.image = self.image1
        self.mask = pygame.mask.from_surface(self.image)    # 用于碰撞检测
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.rect = self.image1.get_rect()
        self.moveFlag = False
        self.delay = 10        # 用于延迟
        self.delay1 = 10
        self.direct = [0, 0, 0, 0]
        self.directMoveFlag = [0, 0, 0, 0]      # 用于人物与墙壁碰撞检测
        self.HP_upper_limit = 100       # 生命值上限
        self.HP_now = 100               # 当前生命值
        self.skill_count = 3            # 技能次数
        self.level = 1
        self.speed = 4
        self.score = 0
        self.initSpeed = self.speed
        self.invincibleFlag = False
        self.invincibleTime = 60
        self.debuff = False
        self.changeDirectFlag = False
        self.reset_status()

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def switchImage(self):
        """
        切换图片，实现动效
        :return: {image} 切换后的图片
        """
        if 1 in self.direct:
            self.moveFlag = True
        else:
            self.moveFlag = False
        # 动作变化循环
        if self.moveFlag:
            if self.delay == 5:
                if self.image == self.image1:
                    self.image = self.image2
                elif self.image == self.image2:
                    self.image = self.image1
            self.delay -= 1
            if self.delay == 0:
                self.delay = 10

    def lifeControler(self, collide_flag):
        """
        英雄生命控制
        :param collide_flag: {bool}是否发生碰撞
        :return:
        """
        damage = collide_flag[0].damage
        if self.HP_now:
            if collide_flag and self.invincibleFlag == False:
                self.HP_now -= damage
                self.invincibleFlag = True
            return True
        if self.HP_now < 0:
            return False

    def invincibleStatus(self):
        if self.invincibleFlag:         # 如果处于无敌状态
            if self.invincibleTime == 0:
                self.invincibleFlag = False
                self.invincibleTime = 60
            self.invincibleTime -= 1
            self.delay1 -= 1
            if self.delay1 == 5:
                return True
            if self.delay1 == 0:
                self.delay1 = 10
            return False
        else:
            return True

    def blitMe(self, flag):               # 绘制
        """
        在指定位置绘制角色
        @:param: flag:{bool} 是否移动
        """
        if flag:
            self.switchImage()
            self.move()
            self.reloadSkill()
        self.drawStatusBar()
        if self.invincibleStatus():
            self.screen.blit(self.image, self.rect)

    def drawStatusBar(self):
        HP_percent = self.HP_now / self.HP_upper_limit * 100
        # 绘制血条
        if HP_percent > 0:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (self.width / 2 - 120, self.height - 30, HP_percent * 2.4, 20))
            self.screen.blit(self.HP_img, (self.width/2 - 120, self.height - 30, 240, 20))
            # 绘制百分比
            HP_text = self.Font_HP.render("%d" % HP_percent+"%", True, (255, 255, 255))
            self.screen.blit(HP_text, (self.width / 2 - 5, self.height - 31))
            self.screen.blit(self.skill_img, (15, self.height - 35))
            # 绘制技能数
            skill_text = self.Font_txt.render("X %d" % self.skill_count, True, (255, 255, 255))
            self.screen.blit(skill_text, (55, self.height - 40))
            # 绘制当前游戏等级
            level_text = self.Font_txt.render("Lv : %d" % self.level, True, (255, 255, 255))
            self.screen.blit(level_text, (self.width - 80, self.height - 40))

    def move(self):
        if self.directMoveFlag[0] == 1:
            if self.rect.top < self.height - 50 - self.rect.height:
                if self.level / 10 > 0:
                    self.rect.top += (1 + int(self.level / 10))
            elif self.rect.top >= self.height - 50 - self.rect.height:
                self.HP_now = 0
        if self.direct[0] == 1 and self.directMoveFlag[0] == 0:
            self.moveUp()
        if self.direct[1] == 1 and self.directMoveFlag[1] == 0:
            self.moveDown()
        if self.direct[2] == 1 and self.directMoveFlag[2] == 0:
            self.moveLeft()
        if self.direct[3] == 1 and self.directMoveFlag[3] == 0:
            self.moveRight()

    def setDirect(self, str_, attitude=False):
        """
        设置移动方向, 控制斜向速度
        :param str_: 移动方向
        :param attitude: 为True时表示：按下某方向
        """
        if not self.changeDirectFlag:
            key = 0
            value = 0    # 键值
            if attitude:
                value = 1
            elif not attitude:
                value = 0
            if str_ == 'up':
                key = 0
            elif str_ == 'down':
                key = 1
            elif str_ == 'left':
                key = 2
            elif str_ == 'right':
                key = 3
            self.direct[key] = value
            # 防止斜向移动速度过快
            if self.direct.count(1) == 2:
                self.speed = self.speed / 2 * 1.7
            else:
                self.speed = self.initSpeed
            # print(self.speed)

    def set_direct_move_flag(self, str_, attitude=False):
        key = 0
        value = 0  # 键值
        if attitude:
            value = 1
        elif not attitude:
            value = 0
        if str_ == 'up':
            key = 0
        elif str_ == 'down':
            key = 1
        elif str_ == 'left':
            key = 2
        elif str_ == 'right':
            key = 3
        self.directMoveFlag[key] = value

    def reset_status(self):
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60  # 减60留给状态栏
        self.HP_upper_limit = 100       # 生命值上限
        self.HP_now = 100               # 当前生命值
        self.skill_count = 3            # 技能次数
        self.level = 1                  # 级别
        self.speed = self.initSpeed

    def getHP(self):
        return self.HP_now

    def upgrade(self, level):
        self.level = level

    def reloadSkill(self):
        score = gl.get_value('score')
        print(score)
        print(self.score)
        if score - self.score > 1500:
            if self.skill_count < 3:
                self.skill_count += 1
            self.score = score

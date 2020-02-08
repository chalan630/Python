'''
@Description: 控制游戏外观和飞船速度属性
@Author: chalan630
@Date: 2020-01-14 20:25:02
@LastEditTime : 2020-02-08 20:19:36
'''


class Settings():
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # 外星人设置
        self.fleet_direction = 1

        # 动态难度
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bullets_allowed = 10
        self.alien_speed_factor = 1
        self.ship_speed_factor = 2.5
        self.fleet_drop_speed = 10          # 到达边缘时，向下移动的速度
        self.alien_points = 50


    def increase_speed(self):
        """初始化随游戏进行变化的设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        if self.bullets_allowed > 4:
            self.bullets_allowed -= 1
        self.alien_points = int(self.alien_points * self.score_scale)
'''
@Description: 控制游戏外观和飞船速度属性
@Author: chalan630
@Date: 2020-01-14 20:25:02
@LastEditTime : 2020-02-08 15:21:30
'''


class Settings():
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10          # 到达边缘时，向下移动的速度
        self.fleet_direction = 1

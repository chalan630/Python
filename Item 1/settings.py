'''
@Descripttion: 控制游戏外观和飞船速度属性
@Author: chalan630
@Date: 2020-01-14 20:25:02
@LastEditTime : 2020-01-16 16:30:56
'''


class Settings():
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2.5

        # 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

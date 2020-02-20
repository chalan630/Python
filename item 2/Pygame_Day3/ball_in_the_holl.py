'''
@Descripttion: 
@Author: chalan630
@Date: 2020-02-20 12:49:50
@LastEditTime: 2020-02-20 15:05:03
'''

import pygame
import sys, os
import math
from random import *

# 继承动画精灵类
class Ball(pygame.sprite.Sprite):
    def __init__(self, ball_image, position, speed, bg_size):
        # 初始化动画精灵
        super(Ball, self).__init__()
        self.ball_image = pygame.image.load(ball_image).convert_alpha()
        self.rect = self.ball_image.get_rect()
        self.rect.left, self.rect.top = position
        self.radius = self.rect.width / 2   # 增加的半径属性
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        # 实现小球从某侧出界，从对侧进来
        if self.rect.right < 0:
            self.rect.left = self.width
        elif self.rect.left > self.width:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = self.height
        elif self.rect.top > self.height:
            self.rect.bottom = 0


# def collide_check(item, target):  # 碰撞检测
#     col_balls = []
#     for each in target:
#         distance = math.sqrt(\
#             math.pow((item.rect.center[0] - each.rect.center[0]), 2) + \
#             math.pow((item.rect.center[1] - each.rect.center[1]), 2))
#         if distance <= (item.rect.width + each.rect.width) / 2:
#             col_balls.append(each)

#     return col_balls    # 返回碰撞的小球

def main():
    os.chdir(sys.path[0])
    pygame.init()
    bg_image = "background.png"
    ball_image = "gray_ball.png"
    running = True

    # 根据背景图片指定游戏界面尺寸大小
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play a ball!")

    background = pygame.image.load(bg_image).convert_alpha()

    # 用来存放小球对象的列表
    balls = []
    group = pygame.sprite.Group()

    # 创建5个球
    BALL_NUM = 5
    for i in range(BALL_NUM):
        # 位置随机，速度随机
        position = randint(0, width - 100), randint(0, height - 100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(ball_image, position, speed, bg_size)
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width - 100), randint(0, height - 100)
        balls.append(ball)
        group.add(ball)

        # while collide_check(ball, balls):# 在创建小球的时候也要进行一次碰撞检测，防止一生成就与别的小球重叠了
        #     ball.rect.left, ball.rect.top = randint(0, width - 100), randint(0, height - 100)
        # balls.append(ball)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
        screen.blit(background, (0, 0))

        for each in balls:
            each.move()
            screen.blit(each.ball_image, each.rect)
        
        # for i in range(BALL_NUM):
        for each in group:
            # item = balls.pop(i) # 取出一个球
            group.remove(each)
            #if collide_check(item, balls):  # 将自己与其他球进行碰撞检测
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]

            # balls.insert(i, item) # 把球放入队列
            group.add(each)

        pygame.display.update()
        clock.tick(60)
    
if __name__ == "__main__":
    main()

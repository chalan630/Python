'''
@Descripttion: 
@Author: chalan630
@Date: 2020-02-20 21:40:45
@LastEditTime: 2020-02-21 14:22:00
'''

import pygame
import sys, os
import math
from random import *

# 继承动画精灵类
class Ball(pygame.sprite.Sprite):
    def __init__(self, gray_ball_image, green_ball_image, position, speed, bg_size, target):
        # 初始化动画精灵
        super(Ball, self).__init__()
        self.gray_ball_image = pygame.image.load(gray_ball_image).convert_alpha()
        self.green_ball_image = pygame.image.load(green_ball_image).convert_alpha()
        self.rect = self.gray_ball_image.get_rect()
        self.rect.left, self.rect.top = position
        self.radius = self.rect.width / 2   # 增加的半径属性
        self.speed = speed
        self.control = False    # 检查小球是否受控制
        self.width, self.height = bg_size[0], bg_size[1]
        self.target = target    # 为每个小球设计不同的目标
    
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

    def check(self, motion):
        # 对每个小球进行检查
        if self.target < motion < self.target + 5:
            return True
        else:
            return False


class Glass(pygame.sprite.Sprite):
    def __init__(self, glass_image, mouse_image, bg_size):
        super(Glass, self).__init__()

        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top = \
            (bg_size[0] - self.glass_rect.width) // 2, \
            bg_size[1] - self.glass_rect.height
        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top =\
            self.glass_rect.left, self.glass_rect.top
        pygame.mouse.set_visible(False)


def main():
    os.chdir(sys.path[0])
    pygame.init()

    # 图片加载
    mouse_image = "src/hand.png"
    bg_image = "src/background.png"
    glass_image = "src/glass.png"
    gray_ball_image = "src/gray_ball.png"
    green_ball_image = "src/green_ball.png"
    running = True

    # 根据背景图片指定游戏界面尺寸大小
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play a ball!")
    background = pygame.image.load(bg_image).convert_alpha()

    # music
    pygame.mixer.music.load("src/bg_music.ogg")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)
    loser_sound = pygame.mixer.Sound("src/loser.wav")
    laugh_sound = pygame.mixer.Sound("src/laugh.wav")
    winner_sound = pygame.mixer.Sound("src/winner.wav")
    hole_sound = pygame.mixer.Sound("src/hole.wav")
    
    # 音乐播放结束则游戏结束
    GAMEOVER = pygame.USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)

    # 用来存放小球对象的列表
    balls = []
    group = pygame.sprite.Group()

    # 创建5个球
    BALL_NUM = 5
    for i in range(BALL_NUM):
        # 位置随机，速度随机
        position = randint(0, width - 100), randint(0, height - 100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(gray_ball_image, green_ball_image, position, speed, bg_size, 5 * (i + 1))
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width - 100), randint(0, height - 100)
        balls.append(ball)
        group.add(ball)

    glass = Glass(glass_image, mouse_image, bg_size)

    motion = 0
    MYTIMER = pygame.USEREVENT + 1
    pygame.time.set_timer(MYTIMER, 1000)
    pygame.key.set_repeat(100, 100)
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(2000)
                laugh_sound.play()
                running = False
            
            elif event.type == MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed = [0, 0]
                            each.control = True
                    motion = 0

            elif event.type == pygame.MOUSEMOTION:
                motion += 1

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -= 1
                if event.key == pygame.K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] += 1
                if event.key == pygame.K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -= 1
                if event.key == pygame.K_d:
                    for each in group:
                        if each.control:
                            each.speed[0] += 1
            
        screen.blit(background, (0, 0))
        screen.blit(glass.glass_image, glass.glass_rect)

        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()
        if glass.mouse_rect.left < glass.glass_rect.left:
            glass.mouse_rect.left = glass.glass_rect.left
        if glass.mouse_rect.left > glass.glass_rect.right - glass.mouse_rect.width:
            glass.mouse_rect.left = glass.glass_rect.right - glass.mouse_rect.width
        if glass.mouse_rect.top < glass.glass_rect.top:
            glass.mouse_rect.top = glass.glass_rect.top
        if glass.mouse_rect.top > glass.glass_rect.bottom - glass.mouse_rect.height:
            glass.mouse_rect.top = glass.glass_rect.bottom - glass.mouse_rect.height

        screen.blit(glass.mouse_image, glass.mouse_rect)
        
        for each in balls:
            each.move()
            if each.control:
                screen.blit(each.green_ball_image, each.rect)
            else:
                screen.blit(each.gray_ball_image, each.rect)
        
        # for i in range(BALL_NUM):
        for each in group:
            # item = balls.pop(i) # 取出一个球
            group.remove(each)
            #if collide_check(item, balls):  # 将自己与其他球进行碰撞检测
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
                each.control = False

            # balls.insert(i, item) # 把球放入队列
            group.add(each)

        pygame.display.update()
        clock.tick(60)
    
if __name__ == "__main__":
    main()

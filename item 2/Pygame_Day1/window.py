'''
@Descripttion: 
@Author: chalan630
@Date: 2020-02-16 15:56:16
@LastEditTime: 2020-02-19 14:00:37
'''
import pygame
import sys, os
from pygame.locals import *
 
# 初始化Pygame
pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255) # RGB 白色

# 全屏探针
fullscreen = False

# 实例化Pygame 的time 模块的 Clock 对象
clock = pygame.time.Clock()
 
# 创建指定大小的窗口 Surface  设置可变尺寸
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

# 设置放大缩小的比例
ratio = 1.0

# 加载图片 加载的图片也是一个 Surface对象
os.chdir(sys.path[0])
oturtle = pygame.image.load("python.bmp")   # 保存原始图像
turtle = oturtle

# 获得图像的位置矩阵
position = position_0 = oturtle.get_rect()   # position_0 保存原始位置

# 获取当前系统最大屏幕尺寸
max_screensize = pygame.display.list_modes()[0]

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                turtle = l_head
                speed = [-1, 0]
            if event.key == pygame.K_RIGHT:
                turtle = r_head
                speed = [1, 0]
            if event.key == pygame.K_UP:
                speed = [0, -1]
            if event.key == pygame.K_DOWN:
                speed = [0, 1]

            # 全屏(F11)
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(max_screensize, pygame.FULLSCREEN | pygame.HWSURFACE)
                    width, height = max_screensize[0], max_screensize[1]
                else:
                    screen = pygame.display.set_mode((600, 400))
                    width, height = 600, 400
                    if position.right > width or position.bottom > height:
                        position = position_0
            
            # 放大缩小，空格恢复原始尺寸
            if event.key == pygame.K_EQUALS or event.key == pygame.K_MINUS or event.key == pygame.K_SPACE:
                # 最大只能放大一倍，缩小50%
                if event.key == pygame.K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == pygame.K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == pygame.K_SPACE:
                    ratio = 1.0
                
                turtle = pygame.transform.smoothscale(oturtle, (int(position_0.width*ratio), int(position_0.height*ratio)))

                # 相应的修改 小蛇的位置和高度
                position.height = int(position_0.height * ratio)
                position.width = int(position_0.width * ratio)

                # 把当前的小蛇赋值给 r_head 或者 l_head
                if speed[0] < 0:
                    l_head = turtle
                    r_head = pygame.transform.flip(turtle, True, False)
                else:
                    r_head = turtle
                    l_head = pygame.transform.flip(turtle, True, False)


        # 用户调整窗口尺寸
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            if position.right > width or position.bottom > height:  # 如果缩小尺寸导致图片出界，复位
                position = turtle.get_rect()

    # 移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False)#水平翻转，垂直不翻转
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()   # surface 对象的 blit()方法将其移动到画布的背景上面的
    # 延迟10毫秒
    # pygame.time.delay(10)
    # 设置帧率
    clock.tick(60)

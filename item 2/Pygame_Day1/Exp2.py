'''
@Descripttion: 
@version: 
@Author: chalan630
@Date: 2020-02-19 13:52:27
@LastEditTime: 2020-02-20 01:13:15
'''
import pygame
import sys, os
from pygame.locals import *

pygame.init()

size = width, height = 600, 400
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Python Demo")
os.chdir(sys.path[0])
turtle = pygame.image.load("Python.bmp")

# 0 未选择 1 选择中 2 完成选择
select = 0
# 初始化选区矩形
select_rect = pygame.Rect(0, 0, 0, 0)
# 0 未拖拽 1 拖拽中 3 完成拖拽
drag = 0

position = turtle.get_rect()
position.center = width // 2, height // 2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        
        # 点击鼠标
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                # 第一次拖拽左键的时候，要裁剪一个范围
                if select == 0 and drag == 0:
                    select = 1
                    pos_start = event.pos
                # 第二次拖拽左键的时候，是表示移动裁剪的图像
                elif select == 2 and drag == 0:
                    drag = 1
                    capture = screen.subsurface(select_rect).copy()
                    cap_rect = capture.get_rect()
                # 第三次点击的时候就是取消选择
                elif select == 2 and drag == 2:
                    select = 0
                    drag = 0

         
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if select == 1 and drag == 0:
                    pos_stop = event.pos
                    select = 2
                elif select == 2 and drag == 1:
                    drag = 2
    
    screen.fill(bg)
    screen.blit(turtle, position)

    if select:
        mouse_pos = pygame.mouse.get_pos()
        if select == 1:
            pos_stop = mouse_pos
        
        select_rect.left, select_rect.top = pos_start
        select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]
        # 调用 draw 模块的 rect() 方法 绘制矩阵
        # rect ( Surface, color, Rect, width = 0)
        pygame.draw.rect(screen, (0, 0, 0), select_rect, 1)

    if drag:
        if drag == 1:
            cap_rect.center = mouse_pos
        screen.blit(capture, cap_rect)

    # flip函数将重新绘制整个屏幕对应的窗口。
    # update函数仅仅重新绘制窗口中有变化的区域。
    pygame.display.update()
    # pygame.display.flip()

    clock.tick(30)
                
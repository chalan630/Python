import pygame
import sys

def check_event(btn):
    # 获取鼠标坐标
    mx, my = pygame.mouse.get_pos()
    # 获取键盘输入，并处理事件
    for event in pygame.event.get():  # 事件循环
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            # 判断鼠标是否移动到按钮范围之内
            btn.getFocus(mx, my)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                btn.mouseDown(mx, my)
        elif event.type == pygame.MOUSEBUTTONUP:
            btn.mouseUp()

def btn_call_back():
    print("我被按下了")


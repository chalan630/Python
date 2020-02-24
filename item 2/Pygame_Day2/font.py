'''
@Descripttion: 
@version: 
@Author: chalan630
@Date: 2020-02-17 12:45:46
@LastEditTime: 2020-02-19 20:16:56
'''

import pygame
import sys

# 初始化Pygame
pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Python Demo")
bg = (0, 0, 0)

position = 0
# 实例化Font对象
font = pygame.font.Font(None, 20)
line_height = font.get_linesize()

screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position += line_height

        if position > height:
            position = 0
            screen.fill(bg)
        
    pygame.display.flip()

'''
@Descripttion: 
@Author: chalan630
@Date: 2020-02-16 16:27:56
@LastEditTime: 2020-02-17 12:42:49
'''

import pygame
import sys
import os

# 初始化Pygame
pygame.init()
size = width, height = 800, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("测试")

# 创建文件，写入形式
os.chdir(sys.path[0])
f = open("recode.txt", "w")

while True:
    for event in pygame.event.get():    # 迭代每一个事件
        f.write(str(event) + '\n')      # 将每一个事件写入文件，以换行符隔开
        if event.type == pygame.QUIT:
            f.close         # 关闭文件
            sys.exit()

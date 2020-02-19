'''
@Descripttion: 
@version: 
@Author: chalan630
@Date: 2020-02-19 22:37:15
@LastEditTime: 2020-02-20 01:03:49
'''

import pygame
import sys
import os
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


size = width, height = 640, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Python Demo")
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
 
    screen.fill(WHITE)    
    
    pygame.draw.ellipse(screen, GREEN, (220, 50, 200, 200), 0)
    pygame.draw.ellipse(screen, BLACK, (100, 100, 440, 100), 1)
 
    pygame.display.flip()
 
    clock.tick(10)

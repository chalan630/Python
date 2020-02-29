'''
@Descripttion: 游戏音频测试
@Author: chalan630
@Date: 2020-02-20 15:21:43
@LastEditTime: 2020-02-21 11:05:41
'''

import pygame
import sys, os

pygame.init()
pygame.mixer.init()

os.chdir(sys.path[0])
pygame.mixer.music.load("src/bg_music.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

cat_sound = pygame.mixer.Sound("src/cat.wav")
cat_sound.set_volume(0.2)
dog_sound = pygame.mixer.Sound("src/dog.wav")
cat_sound.set_volume(0.2)

bg_size = width, height = 300, 200
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Music - Demo")

pause = False

pause_image = pygame.image.load("src/pause.png").convert_alpha()
unpause_image = pygame.image.load("src/unpause.png").convert_alpha()
pause_rect = pause_image.get_rect()
pause_rect.centerx, pause_rect.centery = screen.get_rect().centerx, screen.get_rect().centery

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cat_sound.play()
            elif event.button == 3:
                dog_sound.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
    
    screen.fill((255, 255, 255))

    if pause:
        screen.blit(pause_image, pause_rect)
        pygame.mixer.music.pause()
    else:
        screen.blit(unpause_image, pause_rect)
        pygame.mixer.music.unpause()

    pygame.display.update()

    clock.tick(10)

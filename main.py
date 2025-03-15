import time

import pygame
import sys
import enemy,player


pygame.init()

run_game = True

wight = 200
hight = 300

screen = pygame.display.set_mode((wight,hight))
NIP = enemy.Enemy(screen)
Hero = player.Player(screen)
FPS = 60
clock = pygame.time.Clock()
while run_game:


    Hero.output()
    NIP.output()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(FPS)


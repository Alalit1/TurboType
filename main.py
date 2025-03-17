import json
import pygame
import manu

# Читання конфігурацій з файлу
with open('configs.json', 'r') as f:
    config = json.load(f)

# Доступ до параметрів
width = config['width']
height = config['height']
fullscreen = config['fullscreen']

pygame.init()

run_game = True

if fullscreen:
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((width, height))

manu.main_menu(screen)


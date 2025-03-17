import pygame
import vigets
import sys
import enemy
import player
import random
"""Меню для головного екрану та для ігри"""
enemys =enemy
clock = pygame.time.Clock()
def main_menu(screen):
    buttons = pygame.sprite.Group()
    screen_rect = screen.get_rect()
    list_button = [
        (screen_rect.width/2 - 32, 25, lambda: game(screen), 'Img/Button.png', 'game'),
        (screen_rect.width/2 - 32, 90, lambda: settings(screen), 'Img/Button.png', 'settings'),
        (screen_rect.width/2 - 32, 155, lambda: sys.exit(), 'Img/Button.png', 'exit')
    ]

    for x, y, action, img, text in list_button:
        buttons.add(vigets.Button(x=x, y=y, screen=screen, action=action, image=img, text=text))

    running = True
    while running:
        screen.fill((30, 30, 30))  # Очищення екрану
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            for button in buttons:
                button.upddate([event])  # Обробка подій для кнопок

        for button in buttons:
            button.output()  # Малювання кнопок
        pygame.display.flip()  # Оновлення екрану

        clock.tick(60)  # Обмеження FPS

def settings (screen):
    buttons = pygame.sprite.Group()
    screen_rect = screen.get_rect()
    list_button = [
        (5, 5, lambda: main_menu(screen),'Img/Back.png', ''),
        (screen_rect.width/2 - 32, 50, lambda: sys.exit(), 'Img/Button.png', 'exit')
    ]

    for x, y, action, img, text in list_button:
        buttons.add(vigets.Button(x=x, y=y, screen=screen, action=action,image = img,text=text))

    running = True
    while running:
        screen.fill((30, 30, 30))  # Очищення екрану
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            for button in buttons:
                button.upddate([event])  # Обробка подій для кнопок

        for button in buttons:
            button.output()
         # Малювання кнопок
        pygame.display.flip()  # Оновлення екрану

        clock.tick(60)  # Обмеження FPS

def game (screen):

    NIPS = pygame.sprite.Group()

    Hero = player.Player(screen)
    area_rect = pygame.rect.Rect(50, 50, 750, 550)

    running = True
    while running:

        screen.fill((30, 30, 30))  # Очищення екрану

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            for NIP in NIPS:
                NIP.colade([event])



        NIPS.update()
        # NIPS.draw(screen)

        if len(NIPS) < 5:
            while len(NIPS) < 5:  # Додаємо ворогів, поки їх не 5
                NIPS.add(enemys.Enemy(screen))
        for enemy in NIPS:
            enemy.output()
        rects = [enemy.rect for enemy in NIPS]
        Hero.update(rects)
        Hero.output()
        if Hero.heal_point <=0:
            main_menu(screen)

        pygame.display.flip()  # Оновлення екрану

        clock.tick(60)  # Обмеження FPS
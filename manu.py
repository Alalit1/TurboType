import pygame
import vigets
import sys

import player
import ui
import interfase

"""Меню для головного екрану та для ігри"""


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

        (screen_rect.width / 2 - 32, 12, lambda: sys.exit(), 'Img/Button.png', 'Повний екран'),
        (screen_rect.width / 2 - 32, 80, lambda: sys.exit(), 'Img/Button.png', 'Віконний екран'),
    ]

    for x, y, action, img, text in list_button:
        buttons.add(vigets.Button(x=x, y=y, screen=screen, action=action,image = img,text=text))
    #ff
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

    import enemy

    enemy.Enemy.daed_slaime = 0
    enemys = enemy
    en = enemy.Enemy(screen)


    NIPS = pygame.sprite.Group()

    Hero = player.Player(screen)


    pygame.mixer.init()
    pygame.mixer.music.load('Sound/Manu_music.mp3')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()

    running = True
    while running:

        screen.fill((42, 79, 22))  # Очищення екрану

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.mixer.music.stop()
                sys.exit()

            for NIP in NIPS:
                NIP.colade([event])

        if len(NIPS) < 5:
            while len(NIPS) < 5:  # Додаємо ворогів, поки їх не 5
                NIPS.add(enemys.Enemy(screen))

        for enemy in NIPS:
            enemy.output()

        if Hero.heal_point <=0:
            pygame.mixer.music.stop()
            enemy.get_daed_slaime()
            return

        rects = [enemy.rect for enemy in NIPS]

        NIPS.update()

        Hero.update(rects)
        Hero.output()

        # test.output()
        interfase.game_intefase(screen)
        interfase.count_daed(screen, str(enemy.get_daed_slaime()))
        interfase.score_label(screen, enemy.get_daed_slaime())
        interfase.print_text_label(screen, enemy.get_text_print())
        # for enemy in NIPS:
        #     interfase.score_label(screen,enemy.get_text_print())

        pygame.display.flip()  # Оновлення екрану
        clock.tick(60)  # Обмеження FPS
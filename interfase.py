import pygame
import vigets
import enemy

"""Інтерфейс для ігрока"""

def game_intefase(screen):
    screen_rect = screen.get_rect()

    panel = vigets.Panel(screen=screen, color=(30,30,30),list_pos = [(screen_rect.x, screen_rect.y),
                                                                       (screen_rect.centerx,screen_rect.y),
                                                                       (screen_rect.centerx - 15,screen_rect.y +45),
                                                                       (screen_rect.x,screen_rect.y +45)])
    panel.output()





    img = vigets.Image(screen, 'Img/Slaime.png', (screen_rect.x + 10, 5))
    img.output()
def count_daed(screen,count_daed):
    screen_rect = screen.get_rect()

    label = vigets.Label(screen, (screen_rect.x + 50, 10), (255, 255, 255), count_daed)
    label.output()
def print_text_label(screen,text):
    label = vigets.Label(screen, (400, 50), (255, 255, 255), text)
    label.output()
def score_label(screen,intt):
    screen_rect = screen.get_rect()
    score_all = str(intt * 5)
    label = vigets.Label(screen, (screen_rect.centerx + 50, 5), (255, 255, 255), f"Score :{score_all}")
    label.output()
import pygame.image


class Player():
    def __init__(self,screen):

        """Параметри"""

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
    # TODO: придумать реалізацию різних скінів
        self.img = pygame.image.load('Img/icon.png')
        #self.img = pygame.transform.scale(self.img,(12, 12))
        self.rect = self.img.get_rect()

        self.rect.center = self.screen_rect.center

        # праметри ожно з джейсона вязть

        self.heal_point = 5


    def output(self):
        """Отрисовка"""
        self.screen.blit(self.img,self.rect)

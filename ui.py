import pygame


"""отрисовка дезайна"""
class UI9 ():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.color = (30,30,30)
        # список дезайн + кольор+++оь
    def output(self):
        pygame.draw.polygon(surface=self.screen,color=self.color,points=[(self.screen_rect.x,self.screen_rect.y),
                                                                       (self.screen_rect.centerx,self.screen_rect.y),
                                                                       (self.screen_rect.centerx - 10, self.screen_rect.y + 35),
                                                                       (self.screen_rect.x, self.screen_rect.y + 35)])


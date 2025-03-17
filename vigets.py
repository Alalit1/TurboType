import pygame

"""отрисовка дезайна"""


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, screen,action,image,text):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (100, 64))
        self.rect = self.image.get_rect()

        self.color = (30, 30, 30)

        self.x = x
        self.y = y

        self.rect.x = self.x
        self.rect.y = self.y

        self.action = action

        self.str_text = text
        self.font = pygame.font.SysFont('Arial', 20)
        self.text = self.font.render(self.str_text, True, (255, 255, 255))

        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def upddate(self,event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.action()
    def output(self):
        if self.image == None:
            self.screen.blit(self.color,self.rect)
        else:
            self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text,self.text_rect)

class Slaider():
    def __init__(self, screen, color, image):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.imge = pygame.image.load(image)
        self.rect = self.imge.get_rect()

class Panel():
    def __init__(self, screen, color, image):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.imge = pygame.image.load(image)
        self.rect = self.imge.get_rect()
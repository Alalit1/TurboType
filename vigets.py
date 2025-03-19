import pygame

"""Кнопки та інші елементи інтерфайса (UI)"""


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, screen,action,image,text):
        super().__init__()
        pygame.mixer.init()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (100, 64))
        self.rect = self.image.get_rect()

        self.sound = pygame.mixer.Sound('Sound/Press_button.wav')

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
                self.sound.play()
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
    def __init__(self, screen, color, list_pos):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # self.imge = pygame.image.load(image)
        # self.rect = self.imge.get_rect()

        self.color = color
        self.list_pos = list_pos

    def output(self):
        pygame.draw.polygon(surface=self.screen, color=self.color, points=self.list_pos)
class Label():
    def __init__(self, screen, position, color=(255, 255, 255), text: str = 'Eror'):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.color = color

        self.font = pygame.font.SysFont('Arial', 20)
        self.text = self.font.render(text, True, self.color)
        self.text_rect = self.text.get_rect()

        self.text_rect.x = position[0]
        self.text_rect.y = position[1]

    def output(self):

        self.screen.blit(self.text,self.text_rect)

class Image ():
    def __init__(self, screen, image, position):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.x = position[0]
        self.rect.y = position[1]

    def output(self):

        self.screen.blit(self.image, self.rect)

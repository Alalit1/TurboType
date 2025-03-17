import pygame.image
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.spawned_objects = []
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # TODO: придумать реалізацию різних скінів

        self.image = pygame.image.load('Img/icon.png')
        self.rect = self.image.get_rect()

        # TODO: Придуати реалізацию різних мов для слів
        self.texxt = [
            "Дерево", "Камінь", "Ріка", "Місто", "Птах", "Книга", "Сонце", "Місяць", "Зірка", "Листя",
            "Вітер", "Літо", "Осінь", "Зима", "Весна", "Мрія", "Сміх", "Сльози", "Дружба", "Кохання",
            "Надія", "Сила", "Вогонь", "Льодовик", "Дорога", "Гора", "Острів", "Океан", "Пісня", "Музика",
            "Танець", "Кольори", "Картка", "Світло", "Темрява", "Час", "Простір", "Секунда", "Хвилина", "Година",
            "День", "Ніч", "Ранок", "Вечір", "Сім’я", "Друг", "Ворог", "Мати", "Батько", "Дитина",
            "Школа", "Університет", "Робота", "Кар’єра", "Розмова", "Мова", "Слово", "Ідея", "Мислення", "Наука",
            "Технології", "Комп’ютер", "Інтернет", "Мережа", "Програмування", "Коди", "Система", "Алгоритм", "База",
            "Техніка",
            "Ремонт", "Подорож", "Країна", "Мандрівка", "Відпочинок", "Спорт", "Фітнес", "Вправи", "Змагання", "Погода",
            "Хмара", "Дощ", "Сніг", "Тепло", "Холод", "Шум", "Тиша", "Коханець", "Роман", "Світ",
            "Планета", "Всесвіт", "Космос", "Земля", "Небо", "Дощ", "Пейзаж", "Художник", "Картина", "Творчість"
        ]
        # створення шрифта
        self.font = pygame.font.SysFont('Arial', 20)
        self.text_print = ''

        numbers = random.sample(range(0, 100), 1)  # 5 унікальних чисел від 0 до 100 включн

        self.word = self.texxt[numbers[0]]

        for i in numbers:
            self.text = self.font.render(self.texxt[i], True, (255, 255, 255))

        self.text_rect = self.text.get_rect()


        self.area_rect = pygame.rect.Rect(self.screen_rect.x + 75,
                                          self.screen_rect.x + 75,
                                          self.screen_rect.x + 625,
                                          self.screen_rect.x + 475)

        # TODO: придумать реалізацию випадкового розміщенння в не зони

        # Випадково вибираємо сторону, де буде з'являтися об'єкт
        side = random.choice(["left", "right", "top", "bottom"])

        if side == "left":
            self.rect.x = random.randint(-self.rect.width, -1)
            self.rect.y = random.randint(-self.rect.height, self.area_rect.height + self.rect.height)
        elif side == "right":
            self.rect.x = random.randint(self.area_rect.width, self.area_rect.width + self.rect.width)
            self.rect.y = random.randint(-self.rect.height, self.area_rect.height + self.rect.height)
        elif side == "top":
            self.rect.x = random.randint(-self.rect.width, self.area_rect.width + self.rect.width)
            self.rect.y = random.randint(-self.rect.height, -1)
        elif side == "bottom":
            self.rect.x = random.randint(-self.rect.width, self.area_rect.width + self.rect.width)
            self.rect.y = random.randint(self.area_rect.height, self.area_rect.height + self.rect.height)

        self.speed = 0.2
        self.count = 5

        self.target_rect = (400,300)
        self.velocity = pygame.Vector2(0)
        self.position = (self.rect.x, self.rect.y)

        if (not self.rect.colliderect(self.area_rect) and
                all(not self.rect.colliderect(obj) for obj in self.spawned_objects)):
            self.rect
    def update(self):

        target_pos = pygame.Vector2(self.target_rect)
        nearest_target_vec = pygame.Vector2(target_pos) - self.position
        nearest_target_vec.normalize_ip()


        if self.position != target_pos:
            self.velocity = nearest_target_vec * self.speed
            self.position += self.velocity
            self.rect.center = self.position
        self.text_rect.x = self.rect.x + 5
        self.text_rect.y = self.rect.y - 30

    def colade(self,event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:  # Якщо натиснута клавіша Backspace, видаляємо останній символ
                    self.text_print = self.text_print[:-1]
                elif event.key == pygame.K_RETURN:  # Якщо натиснута клавіша Enter, очищуємо текст
                    self.text_print = ""
                else:
                    self.text_print += event.unicode  # Додаємо натиснуту клавішу до рядка


            if self.text_print == self.word:

                self.kill()

    def output(self):
        """Отрисовка"""

        #pygame.draw.rect(self.screen, color=(255, 0, 255),rect= self.area_rect)
        self.screen.blit(self.image, self.rect)  # Малюємо персонажа
        self.screen.blit(self.text, self.text_rect)


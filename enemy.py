import pygame.image
import random


class Enemy():
    def __init__(self, screen):
        self.spawned_objects = []
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # TODO: придумать реалізацию різних скінів
        self.skin = pygame.image.load('Img/icon.png')
        self.rect = self.skin.get_rect()
        # TODO: Придуати реалізацию різних мов для слів
        self.text = [
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
        self.area_rect = pygame.rect.Rect(10, 10, 10, 10)
        self.corect_pos = '2'
        # текст для відображення
        self.text = self.font.render('Привіт!', True, (255, 255, 255))

        # отримуємо прямокутник тексту
        self.font_rect = self.text.get_rect()
        self.rect.center = self.screen_rect.center

        self.font_rect.bottom = self.rect.top - 5  # 5 пікселів між об'єктом та текстом
        self.font_rect.centerx = self.rect.centerx
        # TODO: придумать реалізацию випадкового розміщенння в не зони

        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = random.randint(0, self.screen_rect.height - self.rect.height)

        if (not self.rect.colliderect(self.area_rect) and
                all(not self.rect.colliderect(obj) for obj in self.spawned_objects)):
            self.rect

    def output(self):
        """Отрисовка"""
        # малюємо зображення
        self.screen.blit(self.skin, self.rect)

        # виводимо текст
        self.screen.blit(self.text, self.font_rect)

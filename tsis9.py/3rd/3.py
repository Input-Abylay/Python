# Импортируем необходимые библиотеки
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Настройка FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Переменные для использования в программе
SCREEN_WIDTH = 390
SCREEN_HEIGHT = 600
SPEED = 5  # Скорость движения врагов
SCORE = 0  # Начальный счет
N = 5  # Количество монет для увеличения скорости врагов
COINS_COLLECTED = 0  # Количество собранных монет

# Настройка фоновой музыки
pygame.mixer.music.load('TSIS_8/resources/fone.wav')
pygame.mixer.music.play(-1)  # Зацикливание воспроизведения

# Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузка фона
background = pygame.image.load("TSIS_8/resources/AnimatedStreet.png")

# Создание экрана
DISPLAYSURF = pygame.display.set_mode((390, 600))
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("TSIS_8/resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("TSIS_8/resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("TSIS_8/resources/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random

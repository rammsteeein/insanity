import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Инициализация экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Простая игра на Pygame")

# Игрок
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 5

# НПС
npc_size = 30
npc_speed = 3
npcs = []

# Функция отрисовки игрока
def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_size, player_size])

# Функция отрисовки НПС
def draw_npc(x, y):
    pygame.draw.rect(screen, red, [x, y, npc_size, npc_size])

# Главный цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Спаун НПС
    if random.randint(0, 100) < 5:
        npc_x = random.randint(0, screen_width - npc_size)
        npc_y = random.randint(0, screen_height - npc_size)
        npcs.append([npc_x, npc_y])

    # Обновление координат НПС
    for npc in npcs:
        if npc[1] < screen_height:
            npc[1] += npc_speed
        else:
            npcs.remove(npc)

    # Проверка столкновения игрока с НПС
    for npc in npcs:
        if (
            player_x < npc[0] + npc_size
            and player_x + player_size > npc[0]
            and player_y < npc[1] + npc_size
            and player_y + player_size > npc[1]
        ):
            npcs.remove(npc)

    # Отрисовка игрока и НПС
    screen.fill(black)
    draw_player(player_x, player_y)
    for npc in npcs:
        draw_npc(npc[0], npc[1])

    pygame.display.update()
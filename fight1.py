import pygame
from d import Alchim
pygame.init()
screen = pygame.display.set_mode((1000, 800))
main_back = pygame.image.load('data/1639284276_12-abrakadabra-fun-p-pikselnaya-tekstura-travi-12.jpg')
hero_idle = pygame.image.load("sprites_gg/idle.png")
hero_idle = pygame.transform.scale(hero_idle, (300, 200))
walk_right = [pygame.image.load(f'sprites_gg/run/Run[{i}].png') for i in range(1, 9)]
walk_left = [pygame.image.load(f'sprites_gg/run1/Run[{i}].png') for i in range(1, 9)]
alchimick = pygame.image.load('data/SNjCmY.png')
alchimick = pygame.transform.scale(alchimick, (200, 250))
castle = pygame.image.load('data/SNjCmY (1).png')
castle = pygame.transform.scale(castle, (200, 250))
animation_list = walk_right  # Start with walk_right animation
animation_steps = 8
last_update = pygame.time.get_ticks()
anim_cd = 50
frame = 0
mp = 500

heroX, heroY = 400, 300
to_left = False
to_right = False
to_up = False
to_down = False
to_attack = False
hp = 500
bit = 1
bit1 = 1
speed = 5
current_frame = pygame.transform.scale(walk_right[frame], (200, 200))
current_frame = pygame.transform.scale(walk_left[frame], (200, 200))
hero_rect = pygame.Rect(heroX, heroY, current_frame.get_width(), current_frame.get_height())
alchimick_rect = pygame.Rect(280, 0, alchimick.get_width(), alchimick.get_height())
castle_rect = pygame.Rect(280, 0, alchimick.get_width(), alchimick.get_height())

clock = pygame.time.Clock()


class Game:
    while True:
        clock.tick(30)
        screen.blit(main_back, (-10, -80))
        pygame.time.delay(1)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    to_left = True
                    animation_list = walk_left
                if event.key == pygame.K_d:
                    to_right = True
                    animation_list = walk_right
                if event.key == pygame.K_s:
                    to_down = True
                    animation_list = walk_right
                if event.key == pygame.K_w:
                    to_up = True
                    animation_list = walk_right
                if event.key == pygame.K_KP_ENTER:
                    print(1)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    to_left = False
                if event.key == pygame.K_d:
                    to_right = False
                if event.key == pygame.K_s:
                    to_down = False
                if event.key == pygame.K_w:
                    to_up = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            hero_rect.topleft = (heroX, heroY)
            # Check for collision after updating the position
            if hero_rect.colliderect(alchimick_rect):
                Alchim()
            if to_right and heroX < 1811:
                heroX += speed
            if to_left and heroX > 0:
                heroX -= speed
            if to_down and heroY < 850:
                heroY += speed
            if to_up and heroY > 0:
                heroY -= speed

        current_time = pygame.time.get_ticks()
        if current_time - last_update > anim_cd:
            frame = (frame + 1) % animation_steps
            last_update = current_time

        if to_right:
            current_frame = pygame.transform.scale(walk_right[frame], (200, 200))

        elif to_left:
            current_frame = pygame.transform.scale(walk_left[frame], (200, 200))
        else:
            current_frame = hero_idle

        screen.blit(current_frame, (heroX, heroY))
        screen.blit(alchimick, (400, 0))
        screen.blit(castle, (100, 300))
        pygame.display.update()
        pygame.display.flip()

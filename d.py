import os
import pygame

pygame.init()
size = width, height = 1083, 698
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
hero = pygame.sprite.Sprite(all_sprites)
hero.image = pygame.image.load(os.path.join('images', 'gg.jpg'))
hvatitzeliy = pygame.sprite.Sprite(all_sprites)
hvatitzeliy.image = pygame.image.load(os.path.join('images', '2zelya.png'))
hero.rect = hero.image.get_rect()
hvatitzeliy.rect = hvatitzeliy.image.get_rect()
taken = pygame.sprite.Sprite(all_sprites)
taken.image = pygame.image.load(os.path.join('images', 'taken.png'))
taken.rect = taken.image.get_rect()
hvatitzeliy.rect.x = -200
taken.rect.x = -200
coords = [0, 0]
running = True
sch = 0
proverkahps = 0
proverkaexp = 0
proverkapov = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = event.pos
            if sch == 2:
                hvatitzeliy.rect.x = 200
                hvatitzeliy.rect.y = 100
            if x_pos >= 430 and x_pos <= 685 and y_pos >= 60 and y_pos <= 320 and sch < 2 and proverkahps == 0:
                print('hps')
                sch += 1
                proverkahps += 1
                taken.rect.x = 600
                taken.rect.y = 70
            if x_pos >= 750 and x_pos <= 1026 and y_pos >= 60 and y_pos <= 320 and sch < 2 and proverkaexp == 0:
                print('exp')
                sch += 1
                proverkaexp += 1
                taken.rect.x = 920
                taken.rect.y = 70
            if x_pos >= 430 and x_pos <= 1026 and y_pos >= 370 and y_pos <= 647 and sch < 2 and proverkapov == 0:
                print('pov')
                sch += 1
                proverkapov += 1
                taken.rect.x = 920
                taken.rect.y = 400




    screen.fill(pygame.Color("blue"))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(200)
pygame.quit()

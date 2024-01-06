import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1000))

hero = pygame.image.load('hero.png')
evilnps = pygame.image.load('npc.png')
evilnps1 = pygame.image.load('npc.png')
heroX, heroY, evilnpsX, evilnpsY, evilnpsX1, evilnpsY1 = 205, 110, 1600, 600, 1600, 200

speed = 2
to_left = False
to_right = False
to_up = False
to_down = False

while True:
    screen.fill((67, 97, 94))
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_left = True
            if event.key == pygame.K_d:
                to_right = True
            if event.key == pygame.K_s:
                to_down = True
            if event.key == pygame.K_w:
                to_up = True

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

    if to_right and heroX < 1811:
        heroX += speed
    if to_left and heroX > 0:
        heroX -= speed
    if to_down and heroY < 850:
        heroY += speed
    if to_up and heroY > 0:
        heroY -= speed

    if heroX > evilnpsX:
        evilnpsX += 1.5
    if heroX < evilnpsX:
        evilnpsX -= 1.5
    if heroY > evilnpsY:
        evilnpsY += 1.5
    if heroY < evilnpsY and evilnpsY > evilnpsY1 + 126:
        evilnpsY -= 1.5

    if heroX > evilnpsX1:
        evilnpsX1 += 1.5
    if heroX < evilnpsX1:
        evilnpsX1 -= 1.5
    if heroY > evilnpsY1 and evilnpsY > evilnpsY1 + 126:
        evilnpsY1 += 1.5
    if heroY < evilnpsY1:
        evilnpsY1 -= 1.5

    screen.blit(hero, (heroX, heroY))
    screen.blit(evilnps, (evilnpsX, evilnpsY))
    screen.blit(evilnps1, (evilnpsX1, evilnpsY1))
    pygame.display.update()


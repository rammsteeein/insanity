import sys

import pygame
from animations import evilnpsanim, bossanim, boomanim, lazeranim, herogoanim, hianim, swordanim, fireanim
from animation import Animation
import pygame as pg
from button import FirstButton


def boss_fight():
    pygame.font.init()
    pygame.init()
    pg.init()
    screen = pygame.display.set_mode((1920, 1080))
    exit_button = FirstButton(1920 / 2 - (200 / 2), 300, 202, 74, '', 'buttons/exit1.png', 'buttons/exit2.png',
                              'buttons/buildingplacement.mp3')

    fone = pygame.image.load('fone.webp')
    boss = pygame.image.load('boss.png')
    hero = Animation(herogoanim, time_interval=16)
    lazer = pygame.image.load('lazer.png')
    died = pygame.image.load('died.jpg')
    heroX, heroY, evilnpsX, evilnpsY, evilnpsX1, evilnpsY1, bossX, bossY, lazerX, lazerY, diedX, fireX, fireY = \
        950, 350, 1600, 600, 1600, 200, 1670, 380, 0, 0, -1920, 1800, 580
    prizov = False
    record = open('record.txt', 'r')
    prizov1 = False
    animschet = 100
    animschetlazer = 0
    speed = 8
    to_left = False
    to_right = False
    to_up = False
    to_down = False
    lazerkill = True
    hp = 500
    bosshp = 500
    bit = 1
    bit1 = 1
    a = 0
    b = 0
    c = 0
    sch = 0
    npsbit = 0
    bossbit = 0
    fire = True
    fire1 = True
    fire2 = True
    lazerflag = False
    fireanimvr = Animation(fireanim, time_interval=12)
    fireanimvr1 = Animation(fireanim, time_interval=12)
    fireanimvr2 = Animation(fireanim, time_interval=12)
    swordanimvr = Animation(swordanim, time_interval=36)
    hianimvr = Animation(hianim, time_interval=50)
    laservr = Animation(lazeranim, time_interval=224)
    npsatackvr = Animation(boomanim, time_interval=100)
    bossanimvr = Animation(bossanim, time_interval=26)
    evilnpsanimvr = Animation(evilnpsanim, time_interval=26)
    sound1 = pg.mixer.Sound('finalstate2.mp3')
    sound2 = pg.mixer.Sound('hi.mp3')
    musicflag = True
    while True:
        sch += 1
        pygame.draw.rect(screen, 'black', (1800, 0, 1920, 1080))
        if sch < 101:
            if musicflag:
                sound2.play()
                musicflag = False
            hianimvr.change(25)
            screen.blit(hianimvr.image, (0, 0))
        if sch >= 101:
            if musicflag is False:
                sound1.play()
                musicflag = True
            screen.blit(fone, (0, 0))
            pygame.time.delay(1)
            screen.blit(boss, (bossX, bossY))
            hero.change(16)
            screen.blit(hero.image, (heroX, heroY))
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
            if hp > 0 and bosshp > 0:

                if to_right and heroX < 1450:
                    heroX += speed
                if to_left and heroX > 240:
                    heroX -= speed
                if to_down and heroY < 880:
                    heroY += speed
                if to_up and heroY > 180:
                    heroY -= speed

                if sch % 1000 == 0:
                    lazerflag = True
                    fire = True
                    a = sch
                if animschetlazer < 225 and sch >= a and sch <= a + 232:

                    fireanimvr.change(6)
                    screen.blit(fireanimvr.image, (fireX - (sch - a) * 10, fireY))
                    if fireX - (sch - a) * 10 in range(heroX, heroX + 109) and fireY in range(heroY,
                                                                                              heroY + 150) and fire:
                        hp -= 100
                        fire = False

                    fireanimvr1.change(6)
                    screen.blit(fireanimvr1.image, (fireX - (sch - a) * 10, fireY + 350))
                    if fireX - (sch - a) * 10 in range(heroX, heroX + 109) and fireY + 350 in range(heroY, heroY + 150) \
                            and fire:
                        hp -= 100
                        fire1 = False

                    fireanimvr2.change(6)
                    screen.blit(fireanimvr2.image, (fireX - (sch - a) * 10, fireY - 350))
                    if fireX - (sch - a) * 10 in range(heroX, heroX + 109) and fireY - 350 in range(heroY, heroY + 150) \
                            and fire:
                        hp -= 100
                        fire2 = False

                    animschetlazer += 1
                    laservr.change(56)
                    screen.blit(laservr.image, (300, 230))
                    if animschetlazer > 32 and (heroX in range(552, 721) or heroX in range(1074, 1238)) and lazerkill \
                            and (heroX + 109 in range(552, 721) or heroX + 109 in range(1074, 1238)):
                        lazerkill = False
                        hp -= 50
                    if animschetlazer > 80 and (heroX not in range(552, 721) or heroX not in range(1074, 1238)) \
                            or (heroX + 109 not in range(552, 721) or heroX + 109 not in range(1074, 1238)):
                        lazerkill = True
                if animschetlazer == 225:
                    animschetlazer = 0
                if sch % 500 == 0:
                    b = sch
                if prizov is False and sch >= b:
                    if heroX > evilnpsX:
                        evilnpsX += 3
                    if heroX < evilnpsX:
                        evilnpsX -= 3
                    if heroY > evilnpsY:
                        evilnpsY += 3
                    if heroY < evilnpsY and evilnpsY > evilnpsY1 + 126:
                        evilnpsY -= 3
                    if (heroX in range(evilnpsX, evilnpsX + 120) and heroY in range(evilnpsY, evilnpsY + 120) or
                        heroX + 108 in range(evilnpsX, evilnpsX) and bit1 == 1 and
                        heroY + 150 in range(evilnpsY, evilnpsY)) and bit == 1:
                        hp -= 10
                        bit *= -1
                        prizov = True
                        evilnpsY = 1200
                        evilnpsX = 1600
                        animschet = 0
                        npsbit += 1
                        if bosshp < 500:
                            bosshp += 50
                    else:
                        evilnpsanimvr.change(5)
                        screen.blit(evilnpsanimvr.image, (evilnpsX, evilnpsY))
                    bossanimvr.change(3)
                    screen.blit(bossanimvr.image, (bossX, bossY))
                if animschet < 100:
                    animschet += 1
                    npsatackvr.change(16)
                    screen.blit(npsatackvr.image, (heroX + 15, heroY + 30))
                if prizov1 is False and sch >= b:
                    if heroX > evilnpsX1:
                        evilnpsX1 += 3
                    if heroX < evilnpsX1:
                        evilnpsX1 -= 3
                    if heroY > evilnpsY1 and evilnpsY > evilnpsY1 + 126:
                        evilnpsY1 += 3
                    if heroY < evilnpsY1:
                        evilnpsY1 -= 3
                    if (heroX in range(evilnpsX1, evilnpsX1 + 120) and heroY in range(evilnpsY1, evilnpsY1 + 120) or
                        heroX + 108 in range(evilnpsX1, evilnpsX1) and bit1 == 1
                        and heroY + 150 in range(evilnpsY1, evilnpsY1)) and bit1 == 1:
                        hp -= 50
                        bit1 *= -1
                        prizov1 = True
                        evilnpsY1 = -200
                        evilnpsX1 = 1600
                        animschet = 0
                        npsbit += 1
                        if bosshp < 500:
                            bosshp += 50
                    else:
                        evilnpsanimvr.change(5)
                        screen.blit(evilnpsanimvr.image, (evilnpsX1, evilnpsY1))
                    bossanimvr.change(3)
                    screen.blit(bossanimvr.image, (bossX, bossY))
                if animschet < 100:
                    animschet += 1
                    npsatackvr.change(16)
                    screen.blit(npsatackvr.image, (heroX + 15, heroY + 30))
                elif prizov is True and prizov1 is True:
                    prizov = False
                    prizov1 = False
                    bit *= -1
                    bit1 *= -1
                    evilnpsY1 = - 200
                if sch % 500 == 0:
                    c = sch
                    bosshp -= 50
                    bossbit += 1

                if sch >= c and sch <= c + 72:
                    swordanimvr.change(9)
                    screen.blit(swordanimvr.image, (bossX + 90, bossY + 100))

                pygame.draw.rect(screen, 'green', (10, 10, hp, 50))
                pygame.draw.rect(screen, 'black', (10, 10, 500, 50), 10)
                pygame.draw.rect(screen, 'red', (1410, 100, bosshp, 50))
                pygame.draw.rect(screen, 'black', (1400, 100, 500, 50), 10)

            if hp <= 0 and diedX < 0:
                diedX += 10
            if bosshp <= 0:
                pygame.draw.rect(screen, 'black', (0, 0, 1920, 1080))

                f1 = pygame.font.Font(None, 248)
                text1 = f1.render('You have won!', True, (0, 255, 0))
                screen.blit(text1, (350, 300))

                f2 = pygame.font.Font(None, 64)
                text2 = f2.render(f'hitting the boss - {bossbit}', True, (180, 0, 0))
                screen.blit(text2, (500, 500))

                text3 = f2.render(f'nps hit you - {npsbit}', True, (180, 0, 0))
                screen.blit(text3, (500, 550))

                text4 = f2.render(f'your record - {record.read()}', True, (180, 0, 0))
                screen.blit(text4, (1300, 800))
                for btn in [exit_button]:
                    btn.handle_event(event)
                if event.type == pygame.USEREVENT and event.button == exit_button:
                    running = False
                    pygame.quit()
                    sys.exit()
            exit_button.check_hover(pygame.mouse.get_pos())
            screen.blit(died, (diedX, 0))
        pygame.display.update()


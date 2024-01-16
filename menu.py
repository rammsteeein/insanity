import pygame
import sys

from button import FirstButton

pygame.init()

pygame.mixer.music.load("sounds/menu.mp3")
main_back = pygame.image.load('data/mount-blade-wallpaper-hd-1920x1080-187426.jpg')
set_back = pygame.image.load('data/settings.jpg')
small_set = pygame.transform.scale(set_back, (700, 700))
cursor_image = pygame.image.load("data/gam379.png")
cursor_rect = cursor_image.get_rect()
pygame.mouse.set_visible(False)

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('insanity v0.1')

play_button = FirstButton(WIDTH / 2 - (200 / 2), 100, 202, 74, '', 'buttons/play1.png', 'buttons/play2.png',
                          'buttons/buildingplacement.mp3')
settings_button = FirstButton(WIDTH / 2 - (252 / 2), 200, 252, 74, '', 'buttons/settings1.png', 'buttons/settings2.png',
                              'buttons/buildingplacement.mp3')
exit_button = FirstButton(WIDTH / 2 - (200 / 2), 300, 202, 74, '', 'buttons/exit1.png', 'buttons/exit2.png',
                          'buttons/buildingplacement.mp3')


def settings_menu():
    running = True
    while running:
        play_button.is_hovered = False
        screen.fill((255, 255, 255))
        screen.blit(small_set, (50, -100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for btn in [exit_button]:
                btn.handle_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        if pygame.mouse.get_focused():
            cursor_x, cursor_y = pygame.mouse.get_pos()
            screen.blit(cursor_image, (cursor_x - cursor_rect.width // 2, cursor_y - cursor_rect.height // 2))
        pygame.display.flip()


def main_menu():
    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(main_back, (-700, -200))

        font = pygame.font.Font('fonts/Minecraft Rus NEW.otf', 72)
        text_surface = font.render('INSANITY', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 60))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for btn in [play_button, settings_button, exit_button]:
                btn.handle_event(event)
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == settings_button:
                settings_menu()
            # if event.type == pygame.USEREVENT and event.button == play_button:
            #     fight1


        exit_button.check_hover(pygame.mouse.get_pos())
        settings_button.check_hover(pygame.mouse.get_pos())
        play_button.check_hover(pygame.mouse.get_pos())
        play_button.draw(screen)
        settings_button.draw(screen)
        exit_button.draw(screen)
        if pygame.mouse.get_focused():
            cursor_x, cursor_y = pygame.mouse.get_pos()
            screen.blit(cursor_image, (cursor_x - cursor_rect.width // 2, cursor_y - cursor_rect.height // 2))
        pygame.display.flip()


main_menu()

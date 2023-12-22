import pygame
import sys
from button import FirstButton

pygame.init()
background =
cursor_image = pygame.image.load("data/gam379.png")
cursor_rect = cursor_image.get_rect()
pygame.mouse.set_visible(False)

WIDTH, HEIGHT = 600, 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('insanity v0.1')

play_button = FirstButton(WIDTH / 2 - (252 / 2), 100, 252, 74, '', 'buttons/play1.png', 'buttons/play2.png',
                          'buttons/buildingplacement.mp3')
settings_button = FirstButton(WIDTH / 2 - (252 / 2), 200, 252, 74, '', 'buttons/settings1.png', 'buttons/settings2.png',
                              'buttons/buildingplacement.mp3')
exit_button = FirstButton(WIDTH / 2 - (252 / 2), 300, 252, 74, '', 'buttons/exit1.png', 'buttons/exit2.png',
                          'buttons/buildingplacement.mp3')


def main_menu():
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            play_button.handle_event(event)
            settings_button.handle_event(event)
            exit_button.handle_event(event)
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

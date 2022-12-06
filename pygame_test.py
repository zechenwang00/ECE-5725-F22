import pygame
import os, sys
import time

# RPi Configs
os.putenv('SDL_VIDEODRIaVER', 'fbcon')   # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb0')
os.putenv('SDL_MOUSEDRV', 'TSLIB')     # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

# Global Flags
code_run = True
detect_run = False
mic_run = False
pir_run = False
main_window = True

# pygame display configs
pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False) # TODO: set to false
WHITE = 255, 255, 255
BLACK = 0,0,0
x,y = 0, 0
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
tick_num = 20
my_font = pygame.font.Font(None, 30)

# button images and their rects
button1_on_img  = pygame.transform.scale(pygame.image.load('./assets/switch_on.png'),  (64, 32))
button2_on_img  = pygame.transform.scale(pygame.image.load('./assets/switch_on.png'),  (64, 32))
button3_on_img  = pygame.transform.scale(pygame.image.load('./assets/switch_on.png'),  (64, 32))
button1_off_img = pygame.transform.scale(pygame.image.load('./assets/switch_off.png'), (64, 32))
button2_off_img = pygame.transform.scale(pygame.image.load('./assets/switch_off.png'), (64, 32))
button3_off_img = pygame.transform.scale(pygame.image.load('./assets/switch_off.png'), (64, 32))

button1_on_rect  = button1_on_img.get_rect(center=(width / 2, 50))
button2_on_rect  = button2_on_img.get_rect(center=(width / 2, 110))
button3_on_rect  = button3_on_img.get_rect(center=(width / 2, 170))
button1_off_rect = button1_on_img.get_rect(center=(width / 2, 50))
button2_off_rect = button2_on_img.get_rect(center=(width / 2, 110))
button3_off_rect = button3_on_img.get_rect(center=(width / 2, 170))

# local photo rects
try:
    photo_img = pygame.transform.scale(pygame.image.load('./sound.jpg'), (256, 144))
    photo_rect = button1_on_img.get_rect(center=(64, 50))
except:
    photo_img = None
    photo_rect = None



while code_run:
    # refresh screen
    screen.fill(WHITE)

    if main_window:
        # if in main menu
        # define buttons and rects
        text_buttons = {'Quit':                 (width * 3 / 4, height - 20),
                        'View Photo':           (width / 4, height - 20),
                        'tracking & stream':    (width / 2, 20),
                        'sound detection':      (width / 2, 80),
                        'PIR alerts':           (width / 2, 140)}
        text_buttons_rect = {}

        img_buttons_rect = {'detect_button': button1_on_rect,
                            'mic_button':    button2_on_rect,
                            'pir_button':    button3_on_rect}


        # blit text rects
        for my_text, text_pos in text_buttons.items():
            text_surface = my_font.render(my_text, True, BLACK)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
            text_buttons_rect[my_text] = rect

        # blit switch rects
        if detect_run:
            screen.blit(button1_on_img, button1_on_rect)
        else:
            screen.blit(button1_off_img, button1_off_rect)
        if mic_run:
            screen.blit(button2_on_img, button2_on_rect)
        else:
            screen.blit(button2_off_img, button2_off_rect)
        if pir_run:
            screen.blit(button3_on_img, button3_on_rect)
        else:
            screen.blit(button3_off_img, button3_off_rect)

        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
            elif (event.type == pygame.MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                x, y = pos
                # checks button collision
                for my_text, rect in text_buttons_rect.items():
                    if rect.collidepoint((x, y)):
                        if my_text == 'Quit':
                            code_run = False
                        elif my_text == 'View Photo':
                            main_window = False
                for button, rect in img_buttons_rect.items():
                    if rect.collidepoint((x, y)):
                        if button == 'detect_button':
                            detect_run = not detect_run
                        elif button == 'mic_button':
                            mic_run = not mic_run
                        elif button == 'pir_button':
                            pir_run = not pir_run
    else:
        # if in photo viewing mode
        text_buttons = {'Back': (width / 2, height - 20)}
        text_buttons_rect = {}
        # blit text rects
        for my_text, text_pos in text_buttons.items():
            text_surface = my_font.render(my_text, True, BLACK)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
            text_buttons_rect[my_text] = rect

        # displays photo
        screen.blit(photo_img, photo_rect)

        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
            elif (event.type == pygame.MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                x, y = pos
                # checks button collision
                for my_text, rect in text_buttons_rect.items():
                    if rect.collidepoint((x, y)):
                        if my_text == 'Back':
                            main_window = True

    pygame.display.flip()
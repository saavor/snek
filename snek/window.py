import pygame

# window stuff
def create_window(width, height):
    DISPLAY = pygame.display.set_mode((width, height), 0, 32)
    return DISPLAY

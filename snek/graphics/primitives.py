import pygame


def rect(self, x, y, width, height, color):
    rect_var = pygame.Rect(x, y, width, height)
    pygame.draw.rect(self.display, color, rect_var)

import pygame


def update_cursor(screen, color, position, size):
    pygame.draw.circle(screen, color, position, size)

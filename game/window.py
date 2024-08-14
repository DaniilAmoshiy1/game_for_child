import asyncio
import pygame

from config import (
    MINIMAL_CURSOR_SIZE,
    MAXIMAL_CURSOR_SIZE,
    STEP_CURSOR_SIZE,
    START_CURSOR_SIZE,
    LEN_BACKGROUND_COLORS,
    LEN_CURSOR_COLORS,
    CURSOR_COLORS,
    BACKGROUND_COLORS
)
from cursor import update_cursor


async def run_game():
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    current_background_color_index = 0

    current_cursor_color_index = 0
    cursor_size = START_CURSOR_SIZE

    pygame.mouse.set_visible(False)

    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_ESCAPE:
                            running = False
                case pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 3:
                            current_background_color_index = (
                                current_background_color_index + 1) % LEN_BACKGROUND_COLORS
                        case 1:
                            current_cursor_color_index = (current_cursor_color_index + 1) % LEN_CURSOR_COLORS
                        case 4:
                            cursor_size = min(MAXIMAL_CURSOR_SIZE, cursor_size + STEP_CURSOR_SIZE)
                        case 5:
                            cursor_size = max(MINIMAL_CURSOR_SIZE, cursor_size - STEP_CURSOR_SIZE)

        screen.fill(BACKGROUND_COLORS[current_background_color_index])
        await asyncio.sleep(0)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        update_cursor(screen, CURSOR_COLORS[current_cursor_color_index], (mouse_x, mouse_y), cursor_size)

        pygame.display.flip()

    pygame.quit()

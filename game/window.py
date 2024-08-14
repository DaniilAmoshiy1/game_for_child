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
    BACKGROUND_COLORS,
    RIGHT_CLICK,
    LEFT_CLICK,
    WHEEL_UP,
    WHEEL_DOWN,
    SCREEN_SIZE
)
from cursor import update_cursor


async def run_game():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)
    current_background_color_index = 0
    current_cursor_color_index = 0
    cursor_size = START_CURSOR_SIZE

    pygame.mouse.set_visible(False)

    event_handlers = {
        pygame.KEYUP: {
            pygame.K_ESCAPE: lambda: None
        },
        pygame.MOUSEBUTTONDOWN: {
            RIGHT_CLICK: lambda: (current_background_color_index + 1) % LEN_BACKGROUND_COLORS,
            LEFT_CLICK: lambda: (current_cursor_color_index + 1) % LEN_CURSOR_COLORS,
            WHEEL_UP: lambda: min(MAXIMAL_CURSOR_SIZE, cursor_size + STEP_CURSOR_SIZE),
            WHEEL_DOWN: lambda: max(MINIMAL_CURSOR_SIZE, cursor_size - STEP_CURSOR_SIZE)
        }
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type in event_handlers:
                if event.type == pygame.KEYUP:
                    if event.key in event_handlers[event.type]:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in event_handlers[event.type]:
                        if event.button == RIGHT_CLICK:
                            current_background_color_index = event_handlers[event.type][event.button]()
                        elif event.button == LEFT_CLICK:
                            current_cursor_color_index = event_handlers[event.type][event.button]()
                        elif event.button == WHEEL_UP:
                            cursor_size = event_handlers[event.type][event.button]()
                        elif event.button == WHEEL_DOWN:
                            cursor_size = event_handlers[event.type][event.button]()

        screen.fill(BACKGROUND_COLORS[current_background_color_index])
        await asyncio.sleep(0)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        update_cursor(screen, CURSOR_COLORS[current_cursor_color_index], (mouse_x, mouse_y), cursor_size)

        pygame.display.flip()

    pygame.quit()


async def main():
    await run_game()

if __name__ == "__main__":
    asyncio.run(main())

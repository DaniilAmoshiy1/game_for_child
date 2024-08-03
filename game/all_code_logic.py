import pygame


def create_window():
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    background_colors = [(200, 255, 200), (255, 200, 200), (200, 200, 255)]
    current_background_color_index = 0

    cursor_color = [(0, 100, 0), (100, 0, 0), (0, 0, 100)]
    current_cursor_color_index = 0
    cursor_size = 50

    pygame.mouse.set_visible(False)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # Правый клик мыши
                    current_background_color_index = (current_background_color_index + 1) % len(background_colors)
                elif event.button == 1:  # Левый клик мыши
                    current_cursor_color_index = (current_cursor_color_index + 1) % len(cursor_color)
                elif event.button == 4:  # Прокрутка колесика вверх
                    cursor_size = min(200, cursor_size + 10)  # Увеличиваем размер, но не более 200
                elif event.button == 5:  # Прокрутка колесика вниз
                    cursor_size = max(50, cursor_size - 10)  # Уменьшаем размер, но не менее 50

        screen.fill(background_colors[current_background_color_index])


        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, cursor_color[current_cursor_color_index], (mouse_x, mouse_y), cursor_size)



        pygame.display.flip()

    pygame.quit()

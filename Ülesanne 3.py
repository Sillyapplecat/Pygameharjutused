import pygame


def draw_grid(screen, square_size, rows, cols, line_color, bg_color):
    screen.fill(bg_color)
    for row in range(rows + 1):
        pygame.draw.line(screen, line_color, (0, row * square_size), (cols * square_size, row * square_size))
    for col in range(cols + 1):
        pygame.draw.line(screen, line_color, (col * square_size, 0), (col * square_size, rows * square_size))


def main():
    pygame.init()

    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Harjutamine")

    square_size = 20
    rows = height // square_size
    cols = width // square_size
    line_color = (255, 0, 0)  # Red grid lines
    bg_color = (144, 238, 144)  # Light green background

    running = True
    while running:
        draw_grid(screen, square_size, rows, cols, line_color, bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
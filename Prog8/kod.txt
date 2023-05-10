import time
import numpy as np
import pygame
import pygame_gui


def update_game(screen, cells, rules, update=False):
    square_size = 20
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    live_rules, dead_rules = prepare_rules(rules)
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]
        color = (10, 10, 10) if cells[row, col] == 0 else (255, 255, 255)

        if cells[row, col] == 1:
            if alive in live_rules:
                updated_cells[row, col] = 1
                if update:
                    color = (255, 255, 255)
            else:
                if update:
                    color = (10, 10, 10)
        else:
            if alive in dead_rules:
                updated_cells[row, col] = 1
                if update:
                    color = (255, 255, 255)

        pygame.draw.rect(screen, color, (col * square_size, (row * square_size), square_size - 1, square_size - 1))

    return updated_cells


def prepare_rules(rules):
    try:
        tmp = rules.strip().split("/")
        live_rules = tuple(int(i) for i in list(tmp[0]))
        dead_rules = tuple(int(i) for i in list(tmp[1]))
        return live_rules, dead_rules
    except:
        return (2, 3), (3,)


def main():
    square_size = 20
    rules = "23/3"
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    manager = pygame_gui.UIManager((600, 600))

    text_entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((0, 600 - square_size), (600, square_size)),
        manager=manager
    )
    rows = 29
    cols = 30
    cells = np.zeros((rows, cols))
    screen.fill((40, 40, 40))

    update_game(screen, cells, rules)
    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update_game(screen, cells, rules)
                    pygame.display.update()
                elif event.key == pygame.K_RETURN:
                    if not running:
                        rules = text_entry.text
                        text_entry.set_text('')

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[0] < 0 or pos[0] > square_size * cols or pos[1] < 0 or pos[1] > square_size * rows:
                    pass
                elif cells[pos[1] // square_size, pos[0] // square_size] == 0:
                    cells[pos[1] // square_size, pos[0] // square_size] = 1
                else:
                    cells[pos[1] // square_size, pos[0] // square_size] = 0

                update_game(screen, cells, rules)
                pygame.display.update()

            manager.process_events(event)

        manager.update(pygame.time.Clock().tick(60) / 1000.0)
        manager.draw_ui(screen)

        if running:
            cells = update_game(screen, cells, rules, update=True)
            pygame.display.update()
            time.sleep(0.2)
        else:
            pygame.display.update()


if __name__ == '__main__':
    main()

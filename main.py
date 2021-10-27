import settings
import gameoflife as gol
import pygame, sys


def draw_cell(x, y, cell):
    x_pixel = x * settings.CELL_SIZE
    y_pixel = y * settings.CELL_SIZE
    pygame.draw.rect(
        screen,
        settings.ALIVE_COLOR if cell else settings.DEAD_COLOR,
        pygame.Rect(x_pixel, y_pixel, settings.CELL_SIZE, settings.CELL_SIZE),
    )

    pygame.draw.rect(
        screen,
        settings.BORDER_COLOR,
        pygame.Rect(x_pixel, y_pixel, settings.CELL_SIZE, settings.CELL_SIZE),
        settings.BORDER_WIDTH,
    )


def draw_board(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            draw_cell(column, row, board[row][column])


def screen_to_board_position(position):
    x, y = position
    x /= settings.CELL_SIZE
    y /= settings.CELL_SIZE
    return int(x), int(y)


if __name__ == "__main__":

    # Initial variables
    board = gol.initBoard()
    paused = False
    # Setting the GUI
    pygame.init()
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    pygame.display.set_caption("Game Of Life")

    # Glider
    board[0][1] = True
    board[1][2] = True
    board[2][0] = True
    board[2][1] = True
    board[2][2] = True

    # 1. Draw board
    # 2. Go over old board cells:
    # 3.    Make decision for each cell and write to new board
    # 4. Replace old board with new
    # 5. Repeat forever

    while True:
        for event in pygame.event.get():
            # Exit safely
            if event.type == pygame.QUIT:
                sys.exit()
            # Get user input
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    paused = not paused

            if any(pygame.mouse.get_pressed()):
                mouse_pos = pygame.mouse.get_pos()
                x, y = screen_to_board_position(mouse_pos)
                board[y][x] = not board[y][x]
                draw_cell(x, y, board[y][x])
                pygame.display.flip()

        if not paused:
            draw_board(board)
            board = gol.makeNextBoard(board)
            pygame.time.delay(int(1 / settings.FRAME_RATE * 1000))
            pygame.display.flip()

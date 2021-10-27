import settings
import gameoflife as gol
import pygame, sys


def drawCell(x, y, cell):
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


def drawBoard(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            drawCell(column, row, board[row][column])


if __name__ == "__main__":

    board = gol.initBoard()

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

    pygame.init()

    screen = pygame.display.set_mode(settings.SCREEN_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        drawBoard(board)
        board = gol.makeNextBoard(board)
        pygame.time.delay(int(1 / settings.FRAME_RATE * 1000))
        pygame.display.flip()

import time
import settings
import gameoflife as gol


def makeBoardOutput(board):
    board_str = ""
    for row in range(len(board)):
        for column in range(len(board[row])):
            board_str += board[row][column]
        board_str += "\n"

    return board_str


if __name__ == "__main__":

    world = []
    board = gol.initBoard()

    # Glider
    board[0][1] = settings.LIVE_CELL
    board[1][2] = settings.LIVE_CELL
    board[2][0] = settings.LIVE_CELL
    board[2][1] = settings.LIVE_CELL
    board[2][2] = settings.LIVE_CELL

    # 1. Print board
    # 2. Go over old board cells:
    # 3.    Make decision for each cell and write to new board
    # 4. Replace old board with new
    # 5. Repeat forever

    while True:
        print(makeBoardOutput(board))
        newBoard = gol.makeNextBoard(board)
        board = newBoard
        time.sleep(1 / settings.FRAME_RATE)

import time
import settings

# TODO: Make the board infinite
BOARD_SIZE_HORIZONTAL = 50
BOARD_SIZE_VERTICAL = 10


def initBoard():
    new_board = []
    for _ in range(BOARD_SIZE_VERTICAL):
        new_row = []
        for _ in range(BOARD_SIZE_HORIZONTAL):
            new_row.append(settings.DEAD_CELL)
        new_board.append(new_row)

    return new_board


def makeNewBoard(board):
    def get_number_of_neighbors(row, column):
        number_of_neighbors = 0

        # Iterating for neighbors while making sure to to check within the board boundaries
        # TODO: For infinite board you can remove boundaries constraints
        for i in range(max(row - 1, 0), min(row + 2, len(board))):
            for j in range(max(column - 1, 0), min(column + 2, len(board[0]))):
                if (i, j) != (row, column):  # Don't count the current cell
                    if board[i][j] == settings.LIVE_CELL:
                        number_of_neighbors += 1

        return number_of_neighbors

    # Rules of life
    # 1. Any live cell with two or three live neighbours survives.
    # 2. Any dead cell with three live neighbours becomes a live cell.
    # 3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

    # My simplification
    # 0-1 = Dead
    # 2 = The Same
    # 3 = Alive
    # 4-8 = Dead

    def decideFateForCell(row, column):
        number_of_neighbors = get_number_of_neighbors(row, column)
        if number_of_neighbors < 2 or 3 < number_of_neighbors:
            return settings.DEAD_CELL
        elif number_of_neighbors == 3:
            return settings.LIVE_CELL
        else:
            return board[row][column]

    next_board = initBoard()
    for row in range(len(board)):
        for column in range(len(board[row])):
            next_board[row][column] = decideFateForCell(row, column)
    return next_board


def makeBoardOutput(board):
    board_str = ""
    for row in range(len(board)):
        for column in range(len(board[row])):
            board_str += board[row][column]
        board_str += "\n"

    return board_str


if __name__ == "__main__":

    board = initBoard()

    # Simple example
    board[5][5] = settings.LIVE_CELL
    board[5][6] = settings.LIVE_CELL
    board[5][7] = settings.LIVE_CELL

    # 1. Print board
    # 2. Go over old board cells:
    # 3.    Make decision for each cell and write to new board
    # 4. Replace old board with new
    # 5. Repeat forever

    while True:
        print(makeBoardOutput(board))
        newBoard = makeNewBoard(board)
        board = newBoard
        time.sleep(1 / settings.FRAME_RATE)

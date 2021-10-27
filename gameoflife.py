import settings


def initBoard():
    new_board = []
    for _ in range(settings.BOARD_HEIGHT):
        new_row = []
        for _ in range(settings.BOARD_WIDTH):
            new_row.append(False)
        new_board.append(new_row)

    return new_board


def _get_number_of_neighbors(board, row, column):
    # Dougnut technique
    def clipToBoard(index, max):
        return 0 if index == max else max + index if index < 0 else index

    number_of_neighbors = 0

    # Iterating for neighbors while making sure to to check within the board boundaries
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if (i, j) != (row, column):  # Don't count the current cell

                i = clipToBoard(i, len(board))
                j = clipToBoard(j, len(board[0]))

                if board[i][j] == True:
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


def _decideFateForCell(board, row, column):
    number_of_neighbors = _get_number_of_neighbors(board, row, column)
    if number_of_neighbors < 2 or 3 < number_of_neighbors:
        return False
    elif number_of_neighbors == 3:
        return True
    else:
        return board[row][column]


def makeNextBoard(board):
    next_board = initBoard()
    for row in range(len(board)):
        for column in range(len(board[row])):
            next_board[row][column] = _decideFateForCell(board, row, column)
    return next_board

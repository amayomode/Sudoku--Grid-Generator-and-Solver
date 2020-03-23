from gridGenerator import make_board


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - - -')
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            if j == 8:
                print('', bo[i][j])
            else:
                print(' ' + str(bo[i][j]) + ' ', end='')


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                pos = (i, j)  # row, col coordinates
                return pos
    return False


def valid(bo, num, pos):
    # Check if the number is found in row, col and sub_squares
    # ignore the position of insertion

    # Cols
    for r in range(len(bo)):
        if bo[r][pos[1]] == num and r != pos[0]:
            return False
    # Rows
    for c in range(len(bo[0])):
        if bo[pos[0]][c] == num and c != pos[1]:
            return False

    # Sub squares
    x = pos[1] // 3
    y = pos[0] // 3
    for r in range(y * 3, y * 3 + 3):
        for c in range(x * 3, x * 3 + 3):
            if bo[r][c] == num and (r, c) != pos:
                return False
    return True


def solve(bo):
    # find empty position board
    # if non exists then the board is solved
    empty = find_empty(bo)
    if not empty:
        return True
    else:
        row, col = empty
    # fill the empty pos with a valid number from (1-9)
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # call solve recursively checking each time if the board is solved
            if solve(bo):
                return True
            # if there is no valid move and board is unsolved set the previous value to 0
            else:
                bo[row][col] = 0

    # board is unsolved
    return False


'''print('\n', '......... Unsolved .........', '\n')

board = make_board()
print_board(board)

print('\n\n', '......... Solved ...........', '\n')

solve(board)
print_board(board)'''

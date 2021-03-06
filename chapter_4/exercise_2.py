#This procedure checks that the most recently placed queen on the board on column
#current does not conflict with existing queens.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        #We have two diagonals hence need the abs()
        if (current - i == abs(board[current] - board[i])):
            return False
    return True


#This procedure places 8 Queens on a board so they don't conflict.
#It assumes n = 8 and won't work with other n!
def EightQueens(n=8, number_of_solutions=1):
    board = [-1] * n
    result = []
    for i in range(n):
        board[0] = i
        for j in range(n):
            board[1] = j
            if not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if not noConflicts(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if noConflicts(board, 7):
                                        result.append(board[:])
    result = result[:number_of_solutions]
    return result

def eight_queens_partial(board):
    all_boards = EightQueens(n = 8, number_of_solutions = 92)
    for candidate in all_boards:
        valid_board = True
        for xi, xj in zip(candidate, board):
            if xj != -1 and xi != xj:
                valid_board = False
        if valid_board:
            return candidate
    return []


if __name__ == '__main__':
    print(eight_queens_partial([-1, 4, -1, -1, -1, -1, -1, 0]))

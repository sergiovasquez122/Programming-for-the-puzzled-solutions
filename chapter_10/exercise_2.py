#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
def nQueens(board):
    rQueens(board, 0, len(board))
    return board

#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current):
    for i in range(len(board)):
        if (i != current and board[i] == board[current]):
            return False
        if (i != current and current - i == abs(board[current] - board[i])):
            return False
    return True


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(board, current, size):
    if (current == size):
        return True
    else:
        if board[current] != -1:
            return rQueens(board, current + 1, size)
        for i in range(size):
            board[current] = i
            if (noConflicts(board, current)):
                done = rQueens(board, current + 1, size)
                if (done):
                    return True
            board[current] = -1
        return False


if __name__ == '__main__':
    board = [-1, -1, 4, -1, -1, -1, -1, 0, -1, 5]
    nQueens(board)
    print(board)

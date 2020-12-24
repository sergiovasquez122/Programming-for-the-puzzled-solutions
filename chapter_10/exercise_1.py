#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
def nQueens(size):
    board = [-1] * size
    rQueens(board, 0, size)
    return board

def pretty_printer(size):
    board = nQueens(size)
    result = ""
    for c in board:
        line_width = len(board) * 2
        line = ['.' if i % 2 == 0 else ' ' for i in range(line_width)]
        line[2 * c] = 'Q'
        result = result + ''.join(str(k) for k in line) + '\n'
    return result

#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(board, current, size):
    if (current == size):
        return True
    else:
        for i in range(size):
            board[current] = i
            if (noConflicts(board, current)):
                done = rQueens(board, current + 1, size)
                if (done):
                    return True
        return False


if __name__ == '__main__':
    print(pretty_printer(8))
    print(pretty_printer(20))

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    return True

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def solve_n_queens(board, col, n):
    if col >= n:
        print_board(board)
        return
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            solve_n_queens(board, col + 1, n)
            board[i][col] = '.'

def print_n_queens_solutions(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)

if __name__ == "__main__":
    n = 5  # Change this to the desired size of the chessboard
    print_n_queens_solutions(n)

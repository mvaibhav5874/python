def is_valid(board, row, col, num):
    # Check if the number is not in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find the first empty cell in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # Find an empty location in the board
    empty_location = find_empty_location(board)

    # If there is no empty location, the puzzle is solved
    if not empty_location:
        return True

    row, col = empty_location

    # Try placing numbers from 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # If the number is valid, place it in the cell
            board[row][col] = num

            # Recursively solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If placing the number leads to an invalid solution, backtrack
            board[row][col] = 0

    # If no number can be placed in the current cell, backtrack
    return False

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Sudoku Solution:")
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")

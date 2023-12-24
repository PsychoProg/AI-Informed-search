"""
Group: 6,
Algorithm: Greedy,
"""
import os

def solve_sudoku(board):
    """ Solve the Sudoku using backtracking """
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        # If no empty cells, the Sudoku is solved
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True
            # undo the choice for invalid solution
            board[row][col] = 0  

    return False

def find_empty_cell(board):
    """ Find the first empty cell in the Sudoku board """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, row, col, num):
    """ Check if placing 'num' in the given cell is valid """
    # Check row, column, and 3x3 subgrid
    return (
        num not in board[row] and
        num not in [board[i][col] for i in range(9)] and
        num not in [board[i][j] for i in range(3 * (row // 3), 3 * (row // 3) + 3) for j in range(3 * (col // 3), 3 * (col // 3) + 3)]
    )

def print_board_to_file(board, filename):
    """ Print the solved Sudoku board to a file """
    with open(filename, 'w') as file:
        for row in board:
            file.write(" ".join(map(str, row)) + "\n")

def read_sudoku_from_file(filename):
    """ Read sudoku board """
    with open(filename, 'r') as file:
        board = [[int(char) for char in line.split()] for line in file]
        return board

if __name__ == "__main__":
    # Create the 'outputs' folder with os lib
    output_folder = 'outputs'
    os.makedirs(output_folder, exist_ok=True)

    input_filename = '1.txt'
    output_filename = 'outputs.txt'

    board = read_sudoku_from_file(input_filename)
    if solve_sudoku(board):
        print(f"Solved Test Case")
        print_board_to_file(board, output_filename)
    else:
        print(f"No solution exists for Test Case")


    # Solve and save Sudoku boards for each test case
    # for i in range(1, 5):
    #     input_filename = f'Test Case/{i}.txt'
    #     output_filename = f'outputs/output{i}.txt'

    #     board = read_sudoku_from_file(input_filename)
    #     if solve_sudoku(board):
    #         print(f"Solved Test Case {i}")
    #         print_board_to_file(board, output_filename)
    #     else:
    #         print(f"No solution exists for Test Case {i}")

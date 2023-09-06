# Contains functions related to solving the Sudoku and generating a new puzzle.

import random


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def generate_puzzle():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(random.randint(12, 24)):
        row, col, num = random.randint(
            0, 8), random.randint(0, 8), random.randint(1, 9)
        while not is_valid(board, row, col, num) or board[row][col] != 0:
            row, col, num = random.randint(
                0, 8), random.randint(0, 8), random.randint(1, 9)
        board[row][col] = num
    return board

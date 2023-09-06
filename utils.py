# Contains utility functions, for example, a function to check if a board is solved.

def is_solved(board):
    for row in board:
        if 0 in row:
            return False
    return True

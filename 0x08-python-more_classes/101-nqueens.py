#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing 
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A chessboard represented by list of lists.
    solutions (list): Containing solutions mande of list of lists.

Solutions are presented in the format [[r, c], [r, c], [r, c], [r, c]],
where 'r' and 'c' denote the row and column, respectively. These pairs
indicate the positions on the chessboard where queens must be placed.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def board_copy(board):
    """Return a deepcopy of a chessboard."""
    return [row.copy() for row in board]


def _solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = [
            [r, c]
            for r, row in enumerate(board)
            for c, val in enumerate(row)
            if val == "Q"
            ]
    return solution


def markedoff(board, row, col):
    """Mared off spots on a chessboard.

    All Makred off spots where non-attacking queens cann't be played anymore.

    Args:
        board (list): The chessboard.
        row (int): The last row where a queen was played.
        col (int): The last column where a queen was played.
    """
    size = len(board)
    # X out forward spots
    for c in range(col + 1, size):
        board[row][c] = "x"
    # X out backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out spots below
    for r in range(row + 1, size):
        board[r][col] = "x"
    # X out spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, size):
        if c >= size:
            break
        board[r][c] = "x"
        c += 1
    # X out spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    # X out spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= size:
            break
        board[r][c] = "x"
        c += 1
    # X out spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, size):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solution(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The working chessboard.
        row (int): The working row.
        queens (int): The number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    size = len(board)
    if queens == size:
        solutions.append(_solution(board))
        return solutions

    for c in range(size):
        if board[row][c] == " ":
            tmp_board = board_copy(board)
            tmp_board[row][c] = "Q"
            markedoff(tmp_board, row, c)
            solutions = recursive_solution(
                    tmp_board,
                    row + 1,
                    queens + 1,
                    solutions
                    )

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board_size = int(sys.argv[1])
    chessboard = init_board(board_size)
    solution_list = recursive_solution(chessboard, 0, 0, [])

    for solution in solution_list:
        print(solution)

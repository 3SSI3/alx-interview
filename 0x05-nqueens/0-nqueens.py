#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed in the given row and column
    # without attacking any other queens.
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(col):
        if col >= N:
            solutions.append([[row, board[row].index(1)] for row in range(N)])
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(col + 1)
                board[row][col] = 0

    solve(0)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == "__main__":
    main()

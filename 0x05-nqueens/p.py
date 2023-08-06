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
            solutions.append([(row, board[row].index(1)) for row in range(N)])
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
        for row in solution:
            print(row, end=' ')
        print()

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


#!/usr/bin/python3

import sys

def is_q(t_sol, sol, col, r, n):
    """
       is_q - Find all posibles solution for N-queen problem and return it
             in a list
       @t_sol: temporaly list to store the all points of a posible solution
       @sol: store all the solution
       @col: save a colum use for a queen
       @i: the row of the chess table
       @n: Number of queens
    """
    if (r > n):
        sol.append(t_sol[:])
        return sol

    for j in range(n + 1):
        if r == 0 or ([r - 1, j - 1] not in t_sol and
                      [r - 1, j + 1] not in t_sol and
                      j not in col):
            if r > 1:
                dia = 0
                for k in range(2, r + 1):
                    if ([r - k, j - k] in t_sol) or ([r - k, j + k] in t_sol):
                        dia = 1
                        break
                if dia:
                    continue
            t_sol.append([r, j])
            col.append(j)
            is_q(t_sol, sol, col, r + 1, n)
            col.pop()
            t_sol.pop()

    return sol


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except BaseException:
        print("N must be a number")
        exit(1)

    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    elif n < 4:
        print("N must be at least 4")
        exit(1)

    is_q_sol = is_q([], [], [], 0, n - 1)
    for r in is_q_sol:
        print(r)
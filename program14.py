
"""
Program: N-Queens Problem Using Backtracking
Author: Saurav 241492

Description:
Places N queens on an N x N chessboard so that no two
queens share the same row, column, or diagonal.

Input: Board dimension n.
Output: All valid board configurations as a list of strings.
"""

from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    if n < 1:
        return []

    solutions = []
    board = [["."] * n for _ in range(n)]

    columns = set()
    diagonals1 = set()  # row - column
    diagonals2 = set()  # row + column

    def backtrack(row: int) -> None:
        if row == n:
            solutions.append(["".join(line) for line in board])
            return

        for col in range(n):
            if (
                col in columns
                or row - col in diagonals1
                or row + col in diagonals2
            ):
                continue

            # Place queen
            board[row][col] = "Q"
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)

            backtrack(row + 1)

            # Remove queen (backtracking)
            board[row][col] = "."
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    backtrack(0)
    return solutions


# Main program
if __name__ == "__main__":
    n = int(input("Enter board dimension n: "))
    solutions = solveNQueens(n)

    print(f"\nTotal solutions: {len(solutions)}")

    for index, solution in enumerate(solutions, start=1):
        print(f"\nSolution {index}:")
        for row in solution:
            print(row)

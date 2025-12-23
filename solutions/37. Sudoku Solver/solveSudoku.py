"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize possible values for each cell
        possible = [
            [set("123456789") if board[i][j] == "." else set() for j in range(9)]
            for i in range(9)
        ]

        # Remove values already on the board from possibilities
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    # Remove from row
                    for k in range(9):
                        possible[i][k].discard(num)
                    # Remove from column
                    for k in range(9):
                        possible[k][j].discard(num)
                    # Remove from 3x3 box
                    box_row, box_col = 3 * (i // 3), 3 * (j // 3)
                    for bi in range(box_row, box_row + 3):
                        for bj in range(box_col, box_col + 3):
                            possible[bi][bj].discard(num)

        def eliminate(row: int, col: int, num: str) -> bool:
            """Remove num from possibilities and propagate constraints"""
            if num not in possible[row][col]:
                return True

            possible[row][col].discard(num)

            # If no possibilities left, contradiction
            if len(possible[row][col]) == 0:
                return False

            # If only one possibility left, assign it
            if len(possible[row][col]) == 1:
                only_num = list(possible[row][col])[0]
                if not assign(row, col, only_num):
                    return False

            return True

        def assign(row: int, col: int, num: str) -> bool:
            """Assign a value and eliminate other possibilities"""
            other_nums = possible[row][col] - {num}

            for other in other_nums:
                if not eliminate(row, col, other):
                    return False

            # Remove num from peers (row, column, box)
            for k in range(9):
                if k != col and not eliminate(row, k, num):
                    return False
            for k in range(9):
                if k != row and not eliminate(k, col, num):
                    return False

            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for bi in range(box_row, box_row + 3):
                for bj in range(box_col, box_col + 3):
                    if (bi, bj) != (row, col) and not eliminate(bi, bj, num):
                        return False

            return True

        def backtrack() -> bool:
            # Find cell with minimum remaining values (MRV heuristic)
            min_cell = None
            min_count = 10

            for i in range(9):
                for j in range(9):
                    if board[i][j] == "." and 0 < len(possible[i][j]) < min_count:
                        min_count = len(possible[i][j])
                        min_cell = (i, j)

            # All cells filled
            if min_cell is None:
                return True

            row, col = min_cell

            # Try each possibility
            for num in list(possible[row][col]):
                # Save state
                old_possible = [
                    [cell.copy() for cell in row_poss] for row_poss in possible
                ]

                # Try assignment
                if assign(row, col, num):
                    board[row][col] = num
                    if backtrack():
                        return True
                    board[row][col] = "."

                # Restore state
                for i in range(9):
                    for j in range(9):
                        possible[i][j] = old_possible[i][j]

            return False

        backtrack()


# Test cases:
if __name__ == "__main__":
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solution.solveSudoku(board)
    for row in board:
        print(row)

    # Expected output:
    """
    ['5', '3', '4', '6', '7', '8', '9', '1', '2']
    ['6', '7', '2', '1', '9', '5', '3', '4', '8']
    ['1', '9', '8', '3', '4', '2', '5', '6', '7']
    ['8', '5', '9', '7', '6', '1', '4', '2', '3']
    ['4', '2', '6', '8', '5', '3', '7', '9', '1']
    ['7', '1', '3', '9', '2', '4', '8', '5', '6']
    ['9', '6', '1', '5', '3', '7', '2', '8', '4']
    ['2', '8', '7', '4', '1', '9', '6', '3', '5']
    ['3', '4', '5', '2', '8', '6', '1', '7', '9']
    """

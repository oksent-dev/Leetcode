"""LeetCode 130: Surrounded Regions.

Problem summary:
Replace every ``O`` region fully enclosed by ``X`` cells with ``X`` in place.
Any ``O`` connected horizontally or vertically to the border must remain.

Source: https://leetcode.com/problems/surrounded-regions/
"""

from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        rows, columns = len(board), len(board[0])
        queue: deque[tuple[int, int]] = deque()

        def mark_safe(row: int, column: int) -> None:
            if board[row][column] == "O":
                board[row][column] = "S"
                queue.append((row, column))

        for row in range(rows):
            mark_safe(row, 0)
            mark_safe(row, columns - 1)
        for column in range(columns):
            mark_safe(0, column)
            mark_safe(rows - 1, column)

        while queue:
            row, column = queue.popleft()
            for row_offset, column_offset in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_offset
                next_column = column + column_offset
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and board[next_row][next_column] == "O"
                ):
                    mark_safe(next_row, next_column)

        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "O":
                    board[row][column] = "X"
                elif board[row][column] == "S":
                    board[row][column] = "O"


if __name__ == "__main__":
    solution = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    solution.solve(board)
    assert board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    single = [["O"]]
    solution.solve(single)
    assert single == [["O"]]
    print("All tests passed.")

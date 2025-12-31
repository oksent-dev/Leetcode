"""
There is a 1-based binary matrix where 0 represents land and 1 represents water.
You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water.
You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells.
You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions
(left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.
"""

from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can_cross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            for d in range(day):
                r, c = cells[d]
                grid[r - 1][c - 1] = 1  # Mark water cells

            visited = [[False] * col for _ in range(row)]

            def dfs(r: int, c: int) -> bool:
                if (
                    r < 0
                    or r >= row
                    or c < 0
                    or c >= col
                    or grid[r][c] == 1
                    or visited[r][c]
                ):
                    return False
                if r == row - 1:
                    return True
                visited[r][c] = True
                return dfs(r + 1, c) or dfs(r - 1, c) or dfs(r, c + 1) or dfs(r, c - 1)

            for c in range(col):
                if grid[0][c] == 0 and dfs(0, c):
                    return True
            return False

        left, right = 1, len(cells)
        last_day = 0

        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                last_day = mid
                left = mid + 1
            else:
                right = mid - 1

        return last_day


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    row1, col1 = 2, 2
    cells1 = [[1, 1], [2, 1], [1, 2], [2, 2]]
    print(solution.latestDayToCross(row1, col1, cells1))  # Output: 2

    row2, col2 = 3, 3
    cells2 = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [3, 2], [2, 3], [1, 3], [3, 1]]
    print(solution.latestDayToCross(row2, col2, cells2))  # Output: 3

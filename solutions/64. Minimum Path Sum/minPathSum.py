"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        # Initialize the first row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # Initialize the first column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Fill in the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(solution.minPathSum(grid1))  # Output: 7

    grid2 = [[1, 2, 3], [4, 5, 6]]
    print(solution.minPathSum(grid2))  # Output: 12

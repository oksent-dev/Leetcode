"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.
Follow up: Could you find an O(n + m) solution?
"""

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if grid[row][col] < 0:
                count += rows - row
                col -= 1
            else:
                row += 1

        return count


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    grid1 = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(solution.countNegatives(grid1))  # Output: 8

    grid2 = [[3, 2], [1, 0]]
    print(solution.countNegatives(grid2))  # Output: 0

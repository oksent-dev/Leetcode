"""
A k x k magic square is a k x k grid filled with integers such that every row sum,
every column sum, and both diagonal sums are all equal.
The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be
found within this grid.
"""

from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Precompute prefix sums for rows and columns
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * (m + 1) for _ in range(n)]

        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
                col_prefix[j][i + 1] = col_prefix[j][i] + grid[i][j]

        def is_magic_square(x: int, y: int, size: int) -> bool:
            target_sum = row_prefix[x][y + size] - row_prefix[x][y]

            # Check rows
            for i in range(x, x + size):
                if row_prefix[i][y + size] - row_prefix[i][y] != target_sum:
                    return False

            # Check columns
            for j in range(y, y + size):
                if col_prefix[j][x + size] - col_prefix[j][x] != target_sum:
                    return False

            # Check main diagonal
            diag_sum = sum(grid[x + i][y + i] for i in range(size))
            if diag_sum != target_sum:
                return False

            # Check anti diagonal
            anti_diag_sum = sum(grid[x + i][y + size - 1 - i] for i in range(size))
            if anti_diag_sum != target_sum:
                return False

            return True

        max_size = 1
        for size in range(2, min(m, n) + 1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if is_magic_square(i, j, size):
                        max_size = size

        return max_size


# Test cases
if __name__ == "__main__":
    solution = Solution()

    grid1 = [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]
    print(solution.largestMagicSquare(grid1))  # Output: 3

    grid2 = [[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]
    print(solution.largestMagicSquare(grid2))  # Output: 2

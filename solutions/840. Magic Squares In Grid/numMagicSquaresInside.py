"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row,
column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
"""

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(r: int, c: int) -> bool:
            nums = set()
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9 or val in nums:
                        return False
                    nums.add(val)

            magic_sum = sum(grid[r][c : c + 3])

            for i in range(3):
                if sum(grid[r + i][c : c + 3]) != magic_sum:
                    return False

            for j in range(3):
                if sum(grid[r + i][c + j] for i in range(3)) != magic_sum:
                    return False

            if sum(grid[r + i][c + i] for i in range(3)) != magic_sum:
                return False

            if sum(grid[r + i][c + 2 - i] for i in range(3)) != magic_sum:
                return False

            return True

        count = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic_square(r, c):
                    count += 1

        return count


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    grid1 = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
    print(solution.numMagicSquaresInside(grid1))  # Output: 1

    grid2 = [[8]]
    print(solution.numMagicSquaresInside(grid2))  # Output: 0

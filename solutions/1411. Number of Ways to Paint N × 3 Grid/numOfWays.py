"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one
of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color
(i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid.
As the answer may grow large, the answer must be computed modulo 10^9 + 7.
"""


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # a: patterns with 2 colors (e.g., RRG, RYY)
        # b: patterns with 3 colors (e.g., RYG, RGY)
        a, b = 6, 6  # For n=1, there are 6 patterns of each type

        for _ in range(2, n + 1):
            new_a = (3 * a + 2 * b) % MOD
            new_b = (2 * a + 2 * b) % MOD
            a, b = new_a, new_b

        return (a + b) % MOD


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    n1 = 1
    print(solution.numOfWays(n1))  # Output: 12

    n2 = 5000
    print(solution.numOfWays(n2))  # Output: 30228214

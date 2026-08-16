"""LeetCode 120: Triangle.

Problem summary:
Find the minimum top-to-bottom path sum in a number triangle. From position
``i`` in one row, the next position must be ``i`` or ``i + 1``.

Source: https://leetcode.com/problems/triangle/
"""


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        best = triangle[-1].copy()

        for row in range(len(triangle) - 2, -1, -1):
            for column, value in enumerate(triangle[row]):
                best[column] = value + min(best[column], best[column + 1])

        return best[0]


if __name__ == "__main__":
    solution = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    original = [row.copy() for row in triangle]
    assert solution.minimumTotal(triangle) == 11
    assert triangle == original
    assert solution.minimumTotal([[-10]]) == -10
    print("All tests passed.")

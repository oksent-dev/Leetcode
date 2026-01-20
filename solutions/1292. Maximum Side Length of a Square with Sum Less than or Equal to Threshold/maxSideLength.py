"""
Given a m x n matrix mat and an integer threshold, return the maximum side-length of a
square with a sum less than or equal to threshold or return 0 if there is no such square.
"""

from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Compute prefix sums
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix_sum[i - 1][j]
                    + prefix_sum[i][j - 1]
                    - prefix_sum[i - 1][j - 1]
                )

        def can_find_square(side: int) -> bool:
            for i in range(side, m + 1):
                for j in range(side, n + 1):
                    total = (
                        prefix_sum[i][j]
                        - prefix_sum[i - side][j]
                        - prefix_sum[i][j - side]
                        + prefix_sum[i - side][j - side]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 0, min(m, n)
        max_side = 0

        while left <= right:
            mid = (left + right) // 2
            if can_find_square(mid):
                max_side = mid
                left = mid + 1
            else:
                right = mid - 1

        return max_side


# Test cases
if __name__ == "__main__":
    solution = Solution()

    mat1 = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]]
    threshold1 = 4
    print(solution.maxSideLength(mat1, threshold1))  # Output: 2

    mat2 = [
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
    ]

    threshold2 = 1
    print(solution.maxSideLength(mat2, threshold2))  # Output: 0

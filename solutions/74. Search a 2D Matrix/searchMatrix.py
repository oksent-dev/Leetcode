"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        n_rows = len(matrix)
        n_cols = len(matrix[0])
        left, right = 0, n_rows * n_cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n_cols][mid % n_cols]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target1 = 3
    print(solution.searchMatrix(matrix1, target1))  # Output: True

    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target2 = 13
    print(solution.searchMatrix(matrix2, target2))  # Output: False

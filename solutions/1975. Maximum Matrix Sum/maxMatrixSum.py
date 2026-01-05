"""
You are given an n x n integer matrix. You can do the following operation any number of times:

- Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
"""

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        total_sum = 0
        negative_count = 0
        min_abs_value = float("inf")

        for i in range(n):
            for j in range(n):
                value = matrix[i][j]
                abs_value = abs(value)
                total_sum += abs_value
                min_abs_value = min(min_abs_value, abs_value)
                if value < 0:
                    negative_count += 1

        # If there's an odd number of negative values, we need to subtract twice the smallest absolute value
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_value

        return total_sum


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    matrix1 = [[-1, -1], [-1, -1]]
    print(solution.maxMatrixSum(matrix1))  # Output: 4

    matrix2 = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
    print(solution.maxMatrixSum(matrix2))  # Output: 16

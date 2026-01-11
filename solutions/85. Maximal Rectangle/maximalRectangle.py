"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        n_cols = len(matrix[0])
        heights = [0] * (n_cols + 1)  # Extra element to handle the stack at the end

        for row in matrix:
            for j in range(n_cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = [-1]  # Initialize stack with a sentinel index
            for i in range(n_cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    matrix1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(solution.maximalRectangle(matrix1))  # Output: 6

    matrix2 = [["0"]]
    print(solution.maximalRectangle(matrix2))  # Output: 0

    matrix3 = [["1"]]
    print(solution.maximalRectangle(matrix3))  # Output: 1

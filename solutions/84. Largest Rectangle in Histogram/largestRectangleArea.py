"""LeetCode 84: Largest Rectangle in Histogram.

Problem summary:
Each integer is the height of a unit-width histogram bar. Return the largest
area of a rectangle made from consecutive bars.

Source: https://leetcode.com/problems/largest-rectangle-in-histogram/
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack: List[tuple[int, int]] = []  # (earliest index, height)

        for index, height in enumerate(heights + [0]):
            start = index
            while stack and stack[-1][1] > height:
                start, previous_height = stack.pop()
                best = max(best, previous_height * (index - start))
            if not stack or stack[-1][1] < height:
                stack.append((start, height))

        return best


if __name__ == "__main__":
    solution = Solution()
    assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert solution.largestRectangleArea([2, 4]) == 4
    assert solution.largestRectangleArea([2, 2, 2]) == 6
    print("All tests passed.")

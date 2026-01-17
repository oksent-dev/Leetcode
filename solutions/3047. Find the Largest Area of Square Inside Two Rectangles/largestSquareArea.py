"""
There exist n rectangles in a 2D plane with edges parallel to the x and y axis.
You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and
 topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.

You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles.
Return 0 if such a square does not exist.
"""

from typing import List


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        n = len(bottomLeft)
        max_area = 0

        # Check all pairs of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # Get intersection coordinates directly
                x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                x2 = min(topRight[i][0], topRight[j][0])
                y2 = min(topRight[i][1], topRight[j][1])

                # Calculate dimensions of intersection
                width = x2 - x1
                height = y2 - y1

                # If valid intersection exists, calculate square area
                if width > 0 and height > 0:
                    side_length = min(width, height)
                    max_area = max(max_area, side_length * side_length)

        return max_area


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    bottomLeft1 = [[1, 1], [2, 2], [3, 1]]
    topRight1 = [[3, 3], [4, 4], [6, 6]]
    print(solution.largestSquareArea(bottomLeft1, topRight1))  # Output: 1

    bottomLeft2 = [[1, 1], [1, 3], [1, 5]]
    topRight2 = [[5, 5], [5, 7], [5, 9]]
    print(solution.largestSquareArea(bottomLeft2, topRight2))  # Output: 4

    bottomLeft3 = [[1, 1], [2, 2], [1, 2]]
    topRight3 = [[3, 3], [4, 4], [3, 4]]
    print(solution.largestSquareArea(bottomLeft3, topRight3))  # Output: 1

    bottomLeft4 = [[1, 1], [3, 3], [3, 1]]
    topRight4 = [[2, 2], [4, 4], [4, 2]]
    print(solution.largestSquareArea(bottomLeft4, topRight4))  # Output: 0

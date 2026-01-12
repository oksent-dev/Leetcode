"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi].
Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
"""

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            total_time += max(dx, dy)

        return total_time


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    points1 = [[1, 1], [3, 4], [-1, 0]]
    print(solution.minTimeToVisitAllPoints(points1))  # Output: 7

    points2 = [[3, 2], [-2, 2]]
    print(solution.minTimeToVisitAllPoints(points2))  # Output: 5

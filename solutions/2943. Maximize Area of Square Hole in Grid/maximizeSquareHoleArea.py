"""
You are given the two integers, n and m and two integer arrays, hBars and vBars.
The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.

You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars.
Note that other bars are fixed and cannot be removed.

Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).
"""

from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def max_consecutive_length(bars: List[int]) -> int:
            """Find the longest sequence of consecutive bars that can be removed."""
            if not bars:
                return 1

            bars = sorted(set(bars))
            max_length = 1
            current_length = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current_length += 1
                    max_length = max(max_length, current_length)
                else:
                    current_length = 1

            return (
                max_length + 1
            )  # +1 because removing n consecutive bars creates a gap of n+1

        max_h_side = max_consecutive_length(hBars)
        max_v_side = max_consecutive_length(vBars)

        max_side = min(max_h_side, max_v_side)
        return max_side * max_side


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    n1, m1 = 2, 1
    hBars1 = [2, 3]
    vBars1 = [2]
    print(solution.maximizeSquareHoleArea(n1, m1, hBars1, vBars1))  # Output: 4

    n2, m2 = 1, 1
    hBars2 = [2]
    vBars2 = [2]
    print(solution.maximizeSquareHoleArea(n2, m2, hBars2, vBars2))  # Output: 4

    n3, m3 = 2, 3
    hBars3 = [2, 3]
    vBars3 = [2, 4]
    print(solution.maximizeSquareHoleArea(n3, m3, hBars3, vBars3))  # Output: 4

    n4, m4 = 3, 2
    hBars4 = [3, 2, 4]
    vBars4 = [3, 2]
    print(solution.maximizeSquareHoleArea(n4, m4, hBars4, vBars4))  # Output: 9

"""
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li]
represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line
equals the total area of the squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted multiple times.
"""

from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        from collections import defaultdict

        # Create events and calculate total area
        events = []
        total_area = 0

        for x, y, l in squares:
            events.append((y, 0, l))  # 0 = square starts (bottom edge)
            events.append((y + l, 1, l))  # 1 = square ends (top edge)
            total_area += l * l

        if not events:
            return 0.0

        events.sort()
        half_area = total_area / 2

        # Sweep line through y-coordinates
        active_widths = defaultdict(int)
        accumulated_area = 0
        prev_y = events[0][0]
        i = 0

        while i < len(events):
            curr_y = events[i][0]

            # Process band from prev_y to curr_y with current active widths
            if prev_y < curr_y and active_widths:
                band_height = curr_y - prev_y
                total_width = sum(
                    width * count for width, count in active_widths.items()
                )
                band_area = total_width * band_height

                if accumulated_area + band_area >= half_area:
                    remaining_area = half_area - accumulated_area
                    line_height = remaining_area / total_width
                    return float(prev_y + line_height)

                accumulated_area += band_area

            # Process all events at curr_y
            while i < len(events) and events[i][0] == curr_y:
                _, event_type, l = events[i]
                if event_type == 0:  # Square starts
                    active_widths[l] += 1
                else:  # Square ends
                    active_widths[l] -= 1
                    if active_widths[l] == 0:
                        del active_widths[l]
                i += 1

            prev_y = curr_y

        return float(prev_y)


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    squares1 = [[0, 0, 1], [2, 2, 1]]
    print(solution.separateSquares(squares1))  # Output: 1.0

    squares2 = [[0, 0, 2], [1, 1, 1]]
    print(solution.separateSquares(squares2))  # Output: 1.16667

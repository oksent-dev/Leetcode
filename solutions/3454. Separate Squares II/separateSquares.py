"""
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li]
represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted only once in this version.
"""

from typing import List
from collections import defaultdict


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def merge_intervals(intervals):
            """Merge overlapping intervals and return total covered width."""
            if not intervals:
                return []

            sorted_intervals = sorted(intervals)
            merged = [sorted_intervals[0]]

            for start, end in sorted_intervals[1:]:
                last_start, last_end = merged[-1]
                if start <= last_end:
                    # Overlapping or adjacent, merge them
                    merged[-1] = (last_start, max(last_end, end))
                else:
                    # Non-overlapping, add as new interval
                    merged.append((start, end))

            return merged

        if not squares:
            return 0.0

        # Create events for sweep line
        events = []

        for x, y, l in squares:
            events.append((y, 0, x, x + l))  # 0 = square starts (bottom edge)
            events.append((y + l, 1, x, x + l))  # 1 = square ends (top edge)

        events.sort()

        # First pass: calculate total covered area
        total_area = 0
        active_intervals = []
        i = 0
        prev_y = events[0][0]

        while i < len(events):
            curr_y = events[i][0]

            if prev_y < curr_y and active_intervals:
                band_height = curr_y - prev_y
                merged = merge_intervals(active_intervals)
                covered_width = sum(end - start for start, end in merged)
                total_area += covered_width * band_height

            while i < len(events) and events[i][0] == curr_y:
                _, event_type, x_start, x_end = events[i]
                if event_type == 0:
                    active_intervals.append((x_start, x_end))
                else:
                    active_intervals.remove((x_start, x_end))
                i += 1

            prev_y = curr_y

        # Second pass: find the separating line
        half_area = total_area / 2
        accumulated_area = 0
        active_intervals = []
        i = 0
        prev_y = events[0][0]

        while i < len(events):
            curr_y = events[i][0]

            # Process band from prev_y to curr_y
            if prev_y < curr_y and active_intervals:
                band_height = curr_y - prev_y
                merged = merge_intervals(active_intervals)
                covered_width = sum(end - start for start, end in merged)
                band_area = covered_width * band_height

                if accumulated_area + band_area >= half_area:
                    remaining_area = half_area - accumulated_area
                    line_height = remaining_area / covered_width
                    return float(prev_y + line_height)

                accumulated_area += band_area

            # Process all events at curr_y
            while i < len(events) and events[i][0] == curr_y:
                _, event_type, x_start, x_end = events[i]
                if event_type == 0:
                    active_intervals.append((x_start, x_end))
                else:
                    active_intervals.remove((x_start, x_end))
                i += 1

            prev_y = curr_y

        return float(prev_y)


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    squares1 = [[0, 0, 1], [2, 2, 1]]
    print(solution.separateSquares(squares1))  # Output: 1.0

    squares2 = [[0, 0, 2], [1, 1, 1]]
    print(solution.separateSquares(squares2))  # Output: 1.0

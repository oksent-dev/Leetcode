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
        # Collect all critical y-coordinates
        y_coords = set()
        total_area = 0

        for x, y, l in squares:
            y_coords.add(y)  # Bottom of square
            y_coords.add(y + l)  # Top of square
            total_area += l * l

        y_coords = sorted(y_coords)
        half_area = total_area / 2
        accumulated_area = 0

        # Process each band between consecutive y-coordinates
        for i in range(len(y_coords) - 1):
            y_bottom = y_coords[i]
            y_top = y_coords[i + 1]
            band_height = y_top - y_bottom

            # Calculate total width of active squares in this band
            active_width = 0
            for x, y, l in squares:
                # Check if this square overlaps with the band [y_bottom, y_top)
                if y < y_top and y + l > y_bottom:
                    active_width += l

            band_area = active_width * band_height

            # Check if the line falls within this band
            if accumulated_area + band_area >= half_area:
                # Interpolate to find exact position within the band
                remaining_area = half_area - accumulated_area
                line_height = remaining_area / active_width if active_width > 0 else 0
                return float(y_bottom + line_height)

            accumulated_area += band_area

        return float(y_coords[-1])  # Fallback


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    squares1 = [[0, 0, 1], [2, 2, 1]]
    print(solution.separateSquares(squares1))  # Output: 1.0

    squares2 = [[0, 0, 2], [1, 1, 1]]
    print(solution.separateSquares(squares2))  # Output: 1.16667

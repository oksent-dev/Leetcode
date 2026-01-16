"""
There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n)
containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and
vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

Return the maximum area of a square field that can be formed by
removing some fences (possibly none) or -1 if it is impossible to make a square field.

Since the answer may be large, return it modulo 109 + 7.

Note: The field is surrounded by two horizontal fences from the coordinates
(1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates
(1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.
"""

from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7

        # Add the boundaries of the field
        hFences = [1] + sorted(hFences) + [m]
        vFences = [1] + sorted(vFences) + [n]

        # Get all possible distances between any two horizontal fences
        h_distances = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_distances.add(hFences[j] - hFences[i])

        # Get all possible distances between any two vertical fences
        v_distances = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_distances.add(vFences[j] - vFences[i])

        # Find the maximum common distance
        common_distances = h_distances & v_distances

        if not common_distances:
            return -1

        max_side = max(common_distances)
        return (max_side * max_side) % MOD


# Test cases
if __name__ == "__main__":
    solution = Solution()

    m1, n1 = 4, 3
    hfences1 = [2, 3]
    vfences1 = [2]
    print(solution.maximizeSquareArea(m1, n1, hfences1, vfences1))  # Expected output: 4

    m2, n2 = 6, 7
    hfences2 = [2]
    vfences2 = [4]
    print(
        solution.maximizeSquareArea(m2, n2, hfences2, vfences2)
    )  # Expected output: -1

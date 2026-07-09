"""
You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n sorted in non-decreasing order, and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [ui, vi], determine whether there exists a path between nodes ui and vi.

Return a boolean array answer, where answer[i] is true if there exists a path between ui and vi in the ith query and false otherwise.
"""

from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        if n == 0:
            return []

        # comp[i] will store the component ID for node i
        comp = [0] * n
        current_component_id = 0

        # Single pass to identify contiguous components
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                current_component_id += 1
            comp[i] = current_component_id

        # For each query, check if both nodes share the same component ID
        return [comp[u] == comp[v] for u, v in queries]


if __name__ == "__main__":
    solution = Solution()

    n1 = 2
    nums1 = [1, 2]
    maxDiff1 = 1
    queries1 = [[0, 0], [0, 1]]
    print(solution.pathExistenceQueries(n1, nums1, maxDiff1, queries1))
    # Output: [True, True]

    n2 = 4
    nums2 = [2, 5, 6, 8]
    maxDiff2 = 2
    queries2 = [[0, 1], [0, 2], [1, 3], [2, 3]]
    print(solution.pathExistenceQueries(n2, nums2, maxDiff2, queries2))
    # Output: [False, False, True, True]

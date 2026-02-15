"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


# Test cases:
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3]
    print(
        sol.subsets(nums1)
    )  # Output: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

    nums2 = [0]
    print(sol.subsets(nums2))  # Output: [[0], []]

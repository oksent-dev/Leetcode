"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current

        return max_global


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums1))  # Output: 6

    nums2 = [1]
    print(solution.maxSubArray(nums2))  # Output: 1

    nums3 = [5, 4, -1, 7, 8]
    print(solution.maxSubArray(nums3))  # Output: 23

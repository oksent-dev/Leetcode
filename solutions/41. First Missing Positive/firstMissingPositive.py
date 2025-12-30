"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Place each number in its right place, i.e., nums[i] = i + 1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # Find the first index i such that nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers are in their correct places, return n + 1
        return n + 1


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 0]
    print(solution.firstMissingPositive(nums1))  # Output: 3

    nums2 = [3, 4, -1, 1]
    print(solution.firstMissingPositive(nums2))  # Output: 2

    nums3 = [7, 8, 9, 11, 12]
    print(solution.firstMissingPositive(nums3))  # Output: 1

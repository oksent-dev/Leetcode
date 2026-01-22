"""
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
"""

from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        arr = nums[:]  # Create a copy to avoid modifying the original

        while len(arr) > 0 and not self._is_non_decreasing(arr):
            # Find the adjacent pair with minimum sum
            min_sum = float("inf")
            min_idx = -1

            for i in range(len(arr) - 1):
                pair_sum = arr[i] + arr[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i

            # Replace the pair with their sum
            if min_idx != -1:
                arr[min_idx] = min_sum
                arr.pop(min_idx + 1)
                operations += 1

        return operations

    def _is_non_decreasing(self, arr: List[int]) -> bool:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [5, 2, 3, 1]
    print(solution.minimumPairRemoval(nums1))  # Output: 2

    nums2 = [1, 2, 2]
    print(solution.minimumPairRemoval(nums2))  # Output: 0

    nums3 = [2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1]
    print(solution.minimumPairRemoval(nums3))  # Output: 9

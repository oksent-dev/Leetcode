"""
You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.
"""

from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        for i in range(n):
            even_seen = set()
            odd_seen = set()
            for j in range(i, n):
                val = nums[j]
                if val % 2 == 0:
                    even_seen.add(val)
                else:
                    odd_seen.add(val)

                if len(even_seen) == len(odd_seen):
                    max_len = max(max_len, j - i + 1)
        return max_len


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, 5, 4, 3]
    print(solution.longestBalanced(nums1))  # Output: 4

    nums2 = [3, 2, 2, 5, 4]
    print(solution.longestBalanced(nums2))  # Output: 5

    nums3 = [1, 2, 3, 2]
    print(solution.longestBalanced(nums3))  # Output: 3

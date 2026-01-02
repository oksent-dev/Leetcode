"""
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.
"""

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1  # This line should never be reached given the problem constraints


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 3]
    print(solution.repeatedNTimes(nums1))  # Output: 3

    nums2 = [2, 1, 2, 5, 3, 2]
    print(solution.repeatedNTimes(nums2))  # Output: 2

    nums3 = [5, 1, 5, 2, 5, 3, 5, 4]
    print(solution.repeatedNTimes(nums3))  # Output: 5

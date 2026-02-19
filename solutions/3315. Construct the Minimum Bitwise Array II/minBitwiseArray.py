"""
You are given an array nums consisting of n prime integers.

You need to construct an array ans of length n, such that, for each index i,
    the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].

Additionally, you must minimize each value of ans[i] in the resulting array.

If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.
"""

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x % 2 == 0:
                ans.append(-1)
            else:
                lowbit_of_x_plus_1 = (x + 1) & -(x + 1)
                ans.append(x ^ (lowbit_of_x_plus_1 >> 1))
        return ans


# Test cases:
if __name__ == "__main__":
    sol = Solution()

    nums1 = [2, 3, 5, 7]
    print(sol.minBitwiseArray(nums1))  # Output: [-1, 1, 4, 3]

    nums2 = [11, 13, 31]
    print(sol.minBitwiseArray(nums2))  # Output: [9, 12, 15]

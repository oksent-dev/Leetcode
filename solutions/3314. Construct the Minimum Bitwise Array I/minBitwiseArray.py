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
        result = []
        for num in nums:
            if num % 2 == 0:  # Even number: impossible to satisfy the condition
                result.append(-1)
            else:
                # Find the rightmost 1 bit followed by a 0 bit, and clear it
                i = 0
                while (num >> i) & 1:  # Count consecutive 1s from LSB
                    i += 1
                # Now bit i is 0, so bit (i-1) is the rightmost 1 before a 0
                ans = num & ~(1 << (i - 1))  # Clear bit (i-1)
                result.append(ans)
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, 3, 5, 7]
    print(solution.minBitwiseArray(nums1))  # Output: [-1, 1, 4, 3]

    nums2 = [11, 13, 31]
    print(solution.minBitwiseArray(nums2))  # Output: [9, 12, 15]

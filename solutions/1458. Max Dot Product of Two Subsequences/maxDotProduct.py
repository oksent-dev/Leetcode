"""
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
"""

from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[float("-inf")] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(
                    dp[i - 1][j], dp[i][j - 1], product, dp[i - 1][j - 1] + product
                )

        return dp[m][n]


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1_1 = [2, 1, -2, 5]
    nums2_1 = [3, 0, -6]
    print(solution.maxDotProduct(nums1_1, nums2_1))  # Output: 18

    nums1_2 = [3, -2]
    nums2_2 = [2, -6, 7]
    print(solution.maxDotProduct(nums1_2, nums2_2))  # Output: 21

    nums1_3 = [-1, -1]
    nums2_3 = [1, 1]
    print(solution.maxDotProduct(nums1_3, nums2_3))  # Output: -1

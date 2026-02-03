"""
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n - 1 such that:

- nums[0...p] is strictly increasing,
- nums[p...q] is strictly decreasing,
- nums[q...n - 1] is strictly increasing.

Return true if nums is trionic, otherwise return false.
"""

from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:  # Need at least 4 elements for valid p and q
            return False

        # Try all possible p and q where 0 < p < q < n-1
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                # Check if nums[0...p] is strictly increasing
                valid = True
                for i in range(p):
                    if nums[i] >= nums[i + 1]:
                        valid = False
                        break
                if not valid:
                    continue

                # Check if nums[p...q] is strictly decreasing
                for i in range(p, q):
                    if nums[i] <= nums[i + 1]:
                        valid = False
                        break
                if not valid:
                    continue

                # Check if nums[q...n-1] is strictly increasing
                for i in range(q, n - 1):
                    if nums[i] >= nums[i + 1]:
                        valid = False
                        break
                if not valid:
                    continue

                # Found valid p and q
                return True

        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 3, 5, 4, 2, 6]
    print(solution.isTrionic(nums1))  # Output: True

    nums2 = [2, 1, 3]
    print(solution.isTrionic(nums2))  # Output: False

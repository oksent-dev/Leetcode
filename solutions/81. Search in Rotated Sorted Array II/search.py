"""LeetCode 81: Search in Rotated Sorted Array II.

Problem summary:
Search for ``target`` in a non-decreasing array that was rotated at an
unknown pivot. Values may be repeated. Return whether the target occurs.

Source: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return True

            # Equal boundary values hide which half is sorted. Discard one
            # copy from each end; this is why the worst case is O(n).
            if nums[left] == nums[middle] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.search([2, 5, 6, 0, 0, 1, 2], 0)
    assert not solution.search([2, 5, 6, 0, 0, 1, 2], 3)
    assert solution.search([1, 0, 1, 1, 1], 0)
    print("All tests passed.")

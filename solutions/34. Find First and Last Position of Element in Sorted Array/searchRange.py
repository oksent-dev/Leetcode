"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirstPosition(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            first_pos = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    first_pos = mid
                    right = mid - 1  # Continue searching in the left half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first_pos

        def findLastPosition(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            last_pos = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    last_pos = mid
                    left = mid + 1  # Continue searching in the right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last_pos

        first_position = findFirstPosition(nums, target)
        last_position = findLastPosition(nums, target)

        return [first_position, last_position]


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    print(solution.searchRange(nums1, target1))  # [3, 4]

    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    print(solution.searchRange(nums2, target2))  # [-1, -1]

    nums3 = []
    target3 = 0
    print(solution.searchRange(nums3, target3))  # [-1, -1]

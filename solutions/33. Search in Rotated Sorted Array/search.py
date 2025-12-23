"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Determine which side is properly sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:  # Target is in the left side
                    right = mid - 1
                else:  # Target is in the right side
                    left = mid + 1
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:  # Target is in the right side
                    left = mid + 1
                else:  # Target is in the left side
                    right = mid - 1

        return -1


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    print(solution.search(nums1, target1))  # 4

    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    print(solution.search(nums2, target2))  # -1

    nums3 = [1]
    target3 = 0
    print(solution.search(nums3, target3))  # -1

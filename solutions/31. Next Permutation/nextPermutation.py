"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible,
the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of arr = [1,2,3] is [1,3,2].
- Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
- While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # Find the first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            # Find the element just larger than nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the elements after index i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3]
    solution.nextPermutation(nums1)
    print(nums1)  # [1, 3, 2]

    nums2 = [3, 2, 1]
    solution.nextPermutation(nums2)
    print(nums2)  # [1, 2, 3]

    nums3 = [1, 1, 5]
    solution.nextPermutation(nums3)
    print(nums3)  # [1, 5, 1]

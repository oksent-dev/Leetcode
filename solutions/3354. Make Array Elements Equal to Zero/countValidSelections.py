"""
You are given an integer array nums.

Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.

After that, you repeat the following process:

If curr is out of the range [0, n - 1], this process ends.
If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
Else if nums[curr] > 0:
Decrement nums[curr] by 1.
Reverse your movement direction (left becomes right and vice versa).
Take a step in your new direction.
A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.

Return the number of possible valid selections.
"""

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] != 0:
                continue

            for direction in [-1, 1]:
                curr = i
                dir = direction
                arr = nums[:]
                valid = True

                while 0 <= curr < n:
                    if arr[curr] == 0:
                        curr += dir
                    else:
                        arr[curr] -= 1
                        dir *= -1
                        curr += dir

                if all(x == 0 for x in arr):
                    count += 1

        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 0, 2, 0, 3]
    print(solution.countValidSelections(nums1))  # 2

    nums2 = [2, 3, 4, 0, 4, 1, 0]
    print(solution.countValidSelections(nums2))  # 0

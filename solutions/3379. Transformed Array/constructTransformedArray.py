"""
You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:

For each index i (where 0 <= i < nums.length), perform the following independent actions:
- If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
- If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
- If nums[i] == 0: Set result[i] to nums[i].
Return the new array result.

Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.

"""

from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n):
            # Calculate the new index using modulo for circular behavior
            new_index = (i + nums[i]) % n
            result.append(nums[new_index])

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    nums1 = [3, -2, 1, 1]
    print(solution.constructTransformedArray(nums1))  # Output: [1, 1, 1, 3]

    nums2 = [-1, 4, -1]
    print(solution.constructTransformedArray(nums2))  # Output: [-1, -1, 4]

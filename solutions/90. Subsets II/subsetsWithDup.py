"""LeetCode 90: Subsets II.

Problem summary:
Return every distinct subset of an integer list that may contain duplicate
values. The result must not contain duplicate subsets.

Source: https://leetcode.com/problems/subsets-ii/
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []
        subset: List[int] = []

        def backtrack(start: int) -> None:
            result.append(subset.copy())
            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index - 1]:
                    continue
                subset.append(nums[index])
                backtrack(index + 1)
                subset.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    actual = solution.subsetsWithDup([1, 2, 2])
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert actual == expected
    assert solution.subsetsWithDup([0]) == [[], [0]]
    print("All tests passed.")

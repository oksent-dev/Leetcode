"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that
sum up to target is less than 150 combinations for the given input.
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remaining - candidates[i], combination, i)
                combination.pop()

        backtrack(target, [], 0)
        return result


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    candidates1 = [2, 3, 6, 7]
    target1 = 7
    print(solution.combinationSum(candidates1, target1))  # [[7], [2, 2, 3]]

    candidates2 = [2, 3, 5]
    target2 = 8
    print(
        solution.combinationSum(candidates2, target2)
    )  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    candidates3 = [2]
    target3 = 1
    print(solution.combinationSum(candidates3, target3))  # []

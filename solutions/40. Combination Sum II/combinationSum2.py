"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtrack(remaining - candidates[i], combination, i + 1)
                combination.pop()

        backtrack(target, [], 0)
        return result


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print(
        solution.combinationSum2(candidates1, target1)
    )  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print(solution.combinationSum2(candidates2, target2))  # [[1, 2, 2], [5]]

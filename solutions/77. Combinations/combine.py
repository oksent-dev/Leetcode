"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start, n + 1):
                backtrack(i + 1, path + [i])

        res = []
        backtrack(1, [])
        return res


# Test cases
solution = Solution()
print(solution.combine(4, 2))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(solution.combine(1, 1))  # [[1]]

"""LeetCode 115: Distinct Subsequences.

Problem summary:
Count how many distinct ways string ``t`` can be obtained from string ``s``
by deleting zero or more characters without changing the remaining order.

Source: https://leetcode.com/problems/distinct-subsequences/
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        ways = [0] * (len(t) + 1)
        ways[0] = 1

        for source_character in s:
            for target_index in range(len(t), 0, -1):
                if source_character == t[target_index - 1]:
                    ways[target_index] += ways[target_index - 1]

        return ways[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.numDistinct("rabbbit", "rabbit") == 3
    assert solution.numDistinct("babgbag", "bag") == 5
    assert solution.numDistinct("abc", "abcd") == 0
    assert solution.numDistinct("abc", "") == 1
    print("All tests passed.")

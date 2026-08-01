"""LeetCode 87: Scramble String.

Problem summary:
A string may be recursively split into two non-empty pieces, with the pieces
optionally swapped at every split. Determine whether ``s2`` can be produced
from ``s1`` by those operations.

Source: https://leetcode.com/problems/scramble-string/
"""

from collections import Counter
from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def matches(first: str, second: str) -> bool:
            if first == second:
                return True
            if Counter(first) != Counter(second):
                return False

            for split in range(1, len(first)):
                without_swap = matches(first[:split], second[:split]) and matches(
                    first[split:], second[split:]
                )
                with_swap = matches(first[:split], second[-split:]) and matches(
                    first[split:], second[:-split]
                )
                if without_swap or with_swap:
                    return True
            return False

        return len(s1) == len(s2) and matches(s1, s2)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isScramble("great", "rgeat")
    assert not solution.isScramble("abcde", "caebd")
    assert solution.isScramble("a", "a")
    print("All tests passed.")

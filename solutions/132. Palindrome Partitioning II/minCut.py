"""LeetCode 132: Palindrome Partitioning II.

Problem summary:
Return the fewest cuts needed to divide a string into substrings that are all
palindromes.

Source: https://leetcode.com/problems/palindrome-partitioning-ii/
"""


class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        palindrome = [False] * length
        minimum_cuts = list(range(length))

        for end in range(length):
            best = end
            for start in range(end + 1):
                is_palindrome = s[start] == s[end] and (
                    end - start <= 2 or palindrome[start + 1]
                )
                palindrome[start] = is_palindrome
                if is_palindrome:
                    best = 0 if start == 0 else min(best, minimum_cuts[start - 1] + 1)
            minimum_cuts[end] = best

        return minimum_cuts[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.minCut("aab") == 1
    assert solution.minCut("a") == 0
    assert solution.minCut("ab") == 1
    assert solution.minCut("abccbc") == 2
    print("All tests passed.")

"""LeetCode 139: Word Break.

Problem summary:
Determine whether a string can be split into one or more dictionary words.
Dictionary entries may be reused.

Source: https://leetcode.com/problems/word-break/
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        maximum_length = max(map(len, words))
        reachable = [False] * (len(s) + 1)
        reachable[0] = True

        for end in range(1, len(s) + 1):
            earliest_start = max(0, end - maximum_length)
            for start in range(earliest_start, end):
                if reachable[start] and s[start:end] in words:
                    reachable[end] = True
                    break

        return reachable[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.wordBreak("leetcode", ["leet", "code"])
    assert solution.wordBreak("applepenapple", ["apple", "pen"])
    assert not solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert solution.wordBreak("aaaaaaa", ["aaaa", "aaa"])
    print("All tests passed.")

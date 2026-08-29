"""LeetCode 140: Word Break II.

Problem summary:
Insert spaces into a string in every possible way such that each token is a
dictionary word. Dictionary entries may be reused.

Source: https://leetcode.com/problems/word-break-ii/
"""

from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)
        maximum_length = max(map(len, words))

        @cache
        def sentences(start: int) -> tuple[str, ...]:
            if start == len(s):
                return ("",)

            result: list[str] = []
            last_end = min(len(s), start + maximum_length)
            for end in range(start + 1, last_end + 1):
                word = s[start:end]
                if word not in words:
                    continue
                for suffix in sentences(end):
                    result.append(word if not suffix else f"{word} {suffix}")
            return tuple(result)

        return list(sentences(0))


if __name__ == "__main__":
    solution = Solution()
    assert set(
        solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    ) == {"cats and dog", "cat sand dog"}
    assert set(
        solution.wordBreak(
            "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
        )
    ) == {
        "pine apple pen apple",
        "pineapple pen apple",
        "pine applepen apple",
    }
    assert solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []
    print("All tests passed.")

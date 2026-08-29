"""LeetCode 131: Palindrome Partitioning.

Problem summary:
Split a string in every possible way such that each resulting substring is a
palindrome, and return all valid partitions.

Source: https://leetcode.com/problems/palindrome-partitioning/
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        length = len(s)
        is_palindrome = [[False] * length for _ in range(length)]

        for start in range(length - 1, -1, -1):
            for end in range(start, length):
                is_palindrome[start][end] = (
                    s[start] == s[end]
                    and (end - start < 2 or is_palindrome[start + 1][end - 1])
                )

        result: list[list[str]] = []
        current: list[str] = []

        def backtrack(start: int) -> None:
            if start == length:
                result.append(current.copy())
                return

            for end in range(start, length):
                if not is_palindrome[start][end]:
                    continue
                current.append(s[start : end + 1])
                backtrack(end + 1)
                current.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert solution.partition("a") == [["a"]]
    assert solution.partition("efe") == [["e", "f", "e"], ["efe"]]
    print("All tests passed.")

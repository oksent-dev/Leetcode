"""LeetCode 91: Decode Ways.

Problem summary:
Digits 1 through 26 map to letters A through Z. Count how many valid ways a
digit string can be decoded; zero is valid only inside 10 or 20.

Source: https://leetcode.com/problems/decode-ways/
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        two_back = one_back = 1
        for index in range(1, len(s)):
            current = 0
            if s[index] != "0":
                current += one_back
            if 10 <= int(s[index - 1 : index + 1]) <= 26:
                current += two_back
            two_back, one_back = one_back, current

        return one_back


if __name__ == "__main__":
    solution = Solution()
    assert solution.numDecodings("12") == 2
    assert solution.numDecodings("226") == 3
    assert solution.numDecodings("06") == 0
    assert solution.numDecodings("2101") == 1
    print("All tests passed.")

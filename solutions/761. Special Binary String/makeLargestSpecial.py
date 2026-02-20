"""
Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
You are given a special binary string s.

A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them.
Two strings are consecutive if the last character of the first string is exactly one index before
the first character of the second string.

Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.
"""


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = i = 0
        res = []
        for j, char in enumerate(s):
            count += 1 if char == "1" else -1
            if count == 0:
                res.append("1" + self.makeLargestSpecial(s[i + 1 : j]) + "0")
                i = j + 1
        return "".join(sorted(res, reverse=True))


# Test cases:
if __name__ == "__main__":
    solution = Solution()
    s1 = "11011000"
    print(solution.makeLargestSpecial(s1))  # Output: "11100100"

    s2 = "10"
    print(solution.makeLargestSpecial(s2))  # Output: "10"

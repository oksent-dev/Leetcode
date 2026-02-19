"""
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans


# Test cases:
if __name__ == "__main__":
    sol = Solution()

    s1 = "00110011"
    print(sol.countBinarySubstrings(s1))  # Output: 6

    s2 = "10101"
    print(sol.countBinarySubstrings(s2))  # Output: 4

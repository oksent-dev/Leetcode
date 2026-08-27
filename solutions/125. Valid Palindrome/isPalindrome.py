"""LeetCode 125: Valid Palindrome.

Problem summary:
Determine whether a phrase reads identically in both directions after case is
ignored and every non-alphanumeric character is skipped.

Source: https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama")
    assert not solution.isPalindrome("race a car")
    assert solution.isPalindrome(" ")
    assert solution.isPalindrome("0P0")
    print("All tests passed.")

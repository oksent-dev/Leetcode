"""
Given a string s, find the length of the longest substring without duplicate characters.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


# Test cases
solution = Solution()

s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))

s = "bbbbb"
print(solution.lengthOfLongestSubstring(s))

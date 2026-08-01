"""LeetCode 97: Interleaving String.

Problem summary:
Determine whether ``s3`` can be formed by merging ``s1`` and ``s2`` while
preserving the original order of the characters from each input string.

Source: https://leetcode.com/problems/interleaving-string/
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # Keep the DP row proportional to the shorter input.
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        possible = [False] * (len(s2) + 1)
        possible[0] = True

        for first_count in range(len(s1) + 1):
            for second_count in range(len(s2) + 1):
                if first_count == second_count == 0:
                    continue
                target_index = first_count + second_count - 1
                take_first = (
                    first_count > 0
                    and possible[second_count]
                    and s1[first_count - 1] == s3[target_index]
                )
                take_second = (
                    second_count > 0
                    and possible[second_count - 1]
                    and s2[second_count - 1] == s3[target_index]
                )
                possible[second_count] = take_first or take_second

        return possible[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    assert not solution.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    assert solution.isInterleave("", "", "")
    assert solution.isInterleave("", "abc", "abc")
    print("All tests passed.")

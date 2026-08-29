"""LeetCode 137: Single Number II.

Problem summary:
Every integer appears exactly three times except one value that appears once.
Return that value in linear time using constant auxiliary space.

Source: https://leetcode.com/problems/single-number-ii/
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for bit in range(32):
            if sum((number >> bit) & 1 for number in nums) % 3:
                result |= 1 << bit

        if result >= 1 << 31:
            result -= 1 << 32
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.singleNumber([2, 2, 3, 2]) == 3
    assert solution.singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
    assert solution.singleNumber([-2, -2, -2, -7]) == -7
    assert solution.singleNumber([-1]) == -1
    print("All tests passed.")

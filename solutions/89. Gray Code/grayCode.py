"""LeetCode 89: Gray Code.

Problem summary:
Return all ``2**n`` n-bit values exactly once, starting at zero, so adjacent
values (including the last and first) differ in exactly one bit.

Source: https://leetcode.com/problems/gray-code/
"""

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [value ^ (value >> 1) for value in range(1 << n)]


def is_valid_gray_code(sequence: List[int], n: int) -> bool:
    return (
        len(sequence) == 1 << n
        and sequence[0] == 0
        and set(sequence) == set(range(1 << n))
        and all(
            ((left ^ right) & ((left ^ right) - 1)) == 0
            for left, right in zip(sequence, sequence[1:] + sequence[:1])
        )
    )


if __name__ == "__main__":
    solution = Solution()
    assert solution.grayCode(2) == [0, 1, 3, 2]
    assert is_valid_gray_code(solution.grayCode(1), 1)
    assert is_valid_gray_code(solution.grayCode(4), 4)
    print("All tests passed.")

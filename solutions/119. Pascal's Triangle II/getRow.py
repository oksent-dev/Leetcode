"""LeetCode 119: Pascal's Triangle II.

Problem summary:
Return the zero-indexed ``rowIndex`` row of Pascal's triangle, where interior
entries equal the sum of the two entries above them.

Source: https://leetcode.com/problems/pascals-triangle-ii/
"""


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for column in range(1, rowIndex + 1):
            next_value = row[-1] * (rowIndex - column + 1) // column
            row.append(next_value)
        return row


if __name__ == "__main__":
    solution = Solution()
    assert solution.getRow(0) == [1]
    assert solution.getRow(1) == [1, 1]
    assert solution.getRow(3) == [1, 3, 3, 1]
    assert solution.getRow(5) == [1, 5, 10, 10, 5, 1]
    print("All tests passed.")

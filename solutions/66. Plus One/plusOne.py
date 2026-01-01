"""
You are given a large integer represented as an integer array digits, where each digits[i]
is the ith digit of the integer. The digits are ordered from most significant to least significant
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Start from the last digit and move backwards
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0

        # If all digits were 9, we need to add a new digit at the front
        return [1] + [0] * n


# Test cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(solution.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
    print(solution.plusOne([9]))  # Output: [1, 0]

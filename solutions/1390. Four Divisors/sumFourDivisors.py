"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
If there is no such integer in the array, return 0.
"""

from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def sum_of_divisors(n: int) -> int:
            divisors = []
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)
                if len(divisors) > 4:
                    return 0
            return sum(divisors) if len(divisors) == 4 else 0

        total_sum = 0
        for num in nums:
            total_sum += sum_of_divisors(num)

        return total_sum


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [21, 4, 7]
    print(solution.sumFourDivisors(nums1))  # Output: 32

    nums2 = [21, 21]
    print(solution.sumFourDivisors(nums2))  # Output: 64

    nums3 = [1, 2, 3, 4, 5]
    print(solution.sumFourDivisors(nums3))  # Output: 0

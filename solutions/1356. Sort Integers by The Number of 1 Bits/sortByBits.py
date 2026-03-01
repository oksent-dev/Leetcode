"""
You are given an integer array arr. 
Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.
"""

from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Test cases:
if __name__ == "__main__":
    solution = Solution()
    arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(solution.sortByBits(arr1))  # Output: [0, 1, 2, 4, 8, 3, 5, 6, 7]

    arr2 = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    print(solution.sortByBits(arr2))  # Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]


"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"
Given n and k, return the k^th permutation sequence.
"""

from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # Create a list of numbers to get numbers from
        numbers = list(range(1, n + 1))
        k -= 1  # Convert k to zero-based index
        permutation = []

        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            permutation.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact

        return "".join(permutation)


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    n1, k1 = 3, 3
    print(solution.getPermutation(n1, k1))  # Output: "213"

    n2, k2 = 4, 9
    print(solution.getPermutation(n2, k2))  # Output: "2314"

    n3, k3 = 3, 1
    print(solution.getPermutation(n3, k3))  # Output: "123"

"""
Given an integer n, return the decimal value of the binary string formed by concatenating 
the binary representations of 1 to n in order, modulo 109 + 7.
"""

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        for i in range(1, n + 1):
            res += bin(i)[2:]
        return int(res, 2) % (10 ** 9 + 7)

# Test cases:
if __name__ == "__main__":
    solution = Solution()
    n1 = 1
    print(solution.concatenatedBinary(n1))  # Output: 1

    n2 = 3
    print(solution.concatenatedBinary(n2))  # Output: 27

    n3 = 12
    print(solution.concatenatedBinary(n3))  # Output: 505379714
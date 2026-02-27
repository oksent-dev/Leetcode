"""
Given the binary representation of an integer as a string s, 
return the number of steps to reduce it to 1 under the following rules:

- If the current number is even, you have to divide it by 2.

- If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.
"""

class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        steps = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                n += 1
            steps += 1
        return steps

# Test cases:
if __name__ == "__main__":
    solution = Solution()
    s1 = "1101"
    print(solution.numSteps(s1))  # Output: 6

    s2 = "10"
    print(solution.numSteps(s2))  # Output: 1

    s3 = "1"
    print(solution.numSteps(s3))  # Output: 0
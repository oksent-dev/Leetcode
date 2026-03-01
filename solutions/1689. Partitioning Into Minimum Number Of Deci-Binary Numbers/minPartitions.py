"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without 
any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, 
return the minimum number of positive deci-binary numbers needed so that they sum up to n.
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))

# Test cases:
if __name__ == "__main__":
    solution = Solution()
    n1 = "32"
    print(solution.minPartitions(n1))  # Output: 3

    n2 = "82734"
    print(solution.minPartitions(n2))  # Output: 8

    n3 = "27346209830709182346"
    print(solution.minPartitions(n3))  # Output: 9
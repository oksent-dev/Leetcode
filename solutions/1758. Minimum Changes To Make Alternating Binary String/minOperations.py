"""
You are given a string s consisting only of the characters '0' and '1'. 
In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal.
For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""

class Solution:
    def minOperations(self, s: str) -> int:
        count0 = 0 # operations to make it "010101..."
        for i, char in enumerate(s):
            if int(char) != i % 2:
                count0 += 1
        
        return min(count0, len(s) - count0)

# Test cases:
if __name__ == "__main__":
    solution = Solution()
    s1 = "0100"
    print(solution.minOperations(s1))  # Output: 1

    s2 = "10"
    print(solution.minOperations(s2))  # Output: 0

    s3 = "1111"
    print(solution.minOperations(s3))  # Output: 2
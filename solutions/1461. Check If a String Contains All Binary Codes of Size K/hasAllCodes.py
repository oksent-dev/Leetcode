"""
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s.
Otherwise, return false.
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set(s[i:i+k] for i in range(len(s) - k + 1))) == 2**k

# Test cases:
if __name__ == "__main__":
    solution = Solution()
    s1 = "00110110"
    k1 = 2
    print(solution.hasAllCodes(s1, k1))  # Output: true

    s2 = "0110"
    k2 = 1
    print(solution.hasAllCodes(s2, k2))  # Output: true

    s3 = "0110"
    k3 = 2
    print(solution.hasAllCodes(s3, k3))  # Output: false

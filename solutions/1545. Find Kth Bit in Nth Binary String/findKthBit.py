"""
Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, 
reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        mid = 1 << (n - 1)
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # In the right half, the bit is the inverted bit from the mirrored position in S_{n-1}
            # The mirrored position for k in the right half of Sn is (2^n - k)
            mirrored_k = (1 << n) - k
            bit = self.findKthBit(n - 1, mirrored_k)
            return "1" if bit == "0" else "0"



# Test cases:
if __name__ == "__main__":
    solution = Solution()
    n1 = 3
    k1 = 1
    print(solution.findKthBit(n1, k1))  # Output: "0"

    n2 = 4
    k2 = 11
    print(solution.findKthBit(n2, k2))  # Output: "1"
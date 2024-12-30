"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += int(num1[i]) * int(num2[j])
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return "".join(map(str, result[::-1]))


# Test cases
s = Solution()
print(s.multiply("2", "3"))  # "6"
print(s.multiply("123", "456"))  # "56088"
print(s.multiply("0", "123"))  # "0"

"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or
the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231,
and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
"""


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        n = len(s)
        sign = 1
        result = 0

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "-" or s[i] == "+"):
            sign = -1 if s[i] == "-" else 1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > (2**31 - 1) // 10 or (
                result == (2**31 - 1) // 10 and digit > 7
            ):
                return 2**31 - 1 if sign == 1 else -(2**31)
            result = result * 10 + digit
            i += 1

        return sign * result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    test_cases = ["42", "   -42", "1337c0d3"]

    for s in test_cases:
        print(f"Input: '{s}' => Output: {solution.myAtoi(s)}")

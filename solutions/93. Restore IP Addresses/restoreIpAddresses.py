"""LeetCode 93: Restore IP Addresses.

Problem summary:
Insert three dots into a string of digits to form every valid IPv4 address.
Each segment must be 0..255 and may not have a leading zero unless it is 0.

Source: https://leetcode.com/problems/restore-ip-addresses/
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result: List[str] = []
        segments: List[str] = []

        def backtrack(index: int) -> None:
            remaining_digits = len(s) - index
            remaining_segments = 4 - len(segments)
            if remaining_digits < remaining_segments or remaining_digits > 3 * remaining_segments:
                return
            if remaining_segments == 0:
                if index == len(s):
                    result.append(".".join(segments))
                return

            for length in range(1, 4):
                segment = s[index : index + length]
                if len(segment) < length:
                    break
                if length > 1 and segment[0] == "0":
                    break
                if int(segment) > 255:
                    break
                segments.append(segment)
                backtrack(index + length)
                segments.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert set(solution.restoreIpAddresses("25525511135")) == {
        "255.255.11.135",
        "255.255.111.35",
    }
    assert solution.restoreIpAddresses("0000") == ["0.0.0.0"]
    assert len(solution.restoreIpAddresses("101023")) == 5
    print("All tests passed.")

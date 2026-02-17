"""
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".
"""

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_ones(n):
            return bin(n).count("1")

        res = []
        for h in range(12):
            for m in range(60):
                if count_ones(h) + count_ones(m) == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res


# Test cases:
if __name__ == "__main__":
    sol = Solution()

    turnedOn1 = 1
    print(
        sol.readBinaryWatch(turnedOn1)
    )  # Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    turnedOn2 = 9
    print(sol.readBinaryWatch(turnedOn2))  # Output: []

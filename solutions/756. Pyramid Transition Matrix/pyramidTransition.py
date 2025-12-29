"""
You are stacking blocks to form a pyramid.
Each block has a color, which is represented by a single letter.
Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed.
A triangular pattern consists of a single block stacked on top of two blocks.
The patterns are given as a list of three-letter strings allowed,
where the first two characters of a pattern represent the left and right bottom blocks respectively,
and the third character is the top block.

For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block.
Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that
every triangular pattern in the pyramid is in allowed, or false otherwise.
"""

from typing import List, Dict, Set


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_map: Dict[str, Set[str]] = {}
        for pattern in allowed:
            key = pattern[:2]
            if key not in allowed_map:
                allowed_map[key] = set()
            allowed_map[key].add(pattern[2])

        def can_build(current_row: str, next_row: str) -> bool:
            if len(current_row) == 1:
                return True

            for i in range(len(current_row) - 1):
                pair = current_row[i : i + 2]
                if pair not in allowed_map:
                    return False

            def backtrack(index: int, new_row: str) -> bool:
                if index == len(current_row) - 1:
                    return can_build(new_row, "")

                pair = current_row[index : index + 2]
                for top_block in allowed_map[pair]:
                    if backtrack(index + 1, new_row + top_block):
                        return True
                return False

            return backtrack(0, "")

        return can_build(bottom, "")


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    bottom1 = "BCD"
    allowed1 = ["BCC", "CDE", "CEA", "FFF"]
    print(solution.pyramidTransition(bottom1, allowed1))  # Output: True

    bottom2 = "AAAA"
    allowed2 = ["AAB", "AAC", "BCD", "BBE", "DEF"]
    print(solution.pyramidTransition(bottom2, allowed2))  # Output: False

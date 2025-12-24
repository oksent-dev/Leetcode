"""
You are given an array apple of size n and an array capacity of size m.

There are n packs where the ith pack contains apple[i] apples.
There are m boxes as well, and the ith box has a capacity of capacity[i] apples.

Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.

Note that, apples from the same pack can be distributed into different boxes.
"""

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)

        boxes_used = 0
        for cap in capacity:
            if total_apples <= 0:
                break
            total_apples -= cap
            boxes_used += 1

        return boxes_used


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    apple1 = [1, 3, 2]
    capacity1 = [4, 3, 1, 5, 2]
    print(solution.minimumBoxes(apple1, capacity1))  # 2

    apple2 = [5, 5, 5]
    capacity2 = [2, 4, 2, 7]
    print(solution.minimumBoxes(apple2, capacity2))  # 4

"""LeetCode 135: Candy.

Problem summary:
Give every child at least one candy while ensuring a child with a higher
rating than an adjacent child receives more. Return the minimum total.

Source: https://leetcode.com/problems/candy/
"""


class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)

        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index - 1]:
                candies[index] = candies[index - 1] + 1

        for index in range(len(ratings) - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                candies[index] = max(candies[index], candies[index + 1] + 1)

        return sum(candies)


if __name__ == "__main__":
    solution = Solution()
    assert solution.candy([1, 0, 2]) == 5
    assert solution.candy([1, 2, 2]) == 4
    assert solution.candy([1, 3, 4, 5, 2]) == 11
    assert solution.candy([1]) == 1
    print("All tests passed.")

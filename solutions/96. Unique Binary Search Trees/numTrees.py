"""LeetCode 96: Unique Binary Search Trees.

Problem summary:
Count the structurally distinct binary search trees that store values 1
through ``n``. Each possible root combines every left and right subtree.

Source: https://leetcode.com/problems/unique-binary-search-trees/
"""


class Solution:
    def numTrees(self, n: int) -> int:
        counts = [0] * (n + 1)
        counts[0] = 1

        for nodes in range(1, n + 1):
            for left_size in range(nodes):
                right_size = nodes - left_size - 1
                counts[nodes] += counts[left_size] * counts[right_size]

        return counts[n]


if __name__ == "__main__":
    solution = Solution()
    assert solution.numTrees(1) == 1
    assert solution.numTrees(3) == 5
    assert solution.numTrees(5) == 42
    print("All tests passed.")

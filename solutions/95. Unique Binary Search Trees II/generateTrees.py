"""LeetCode 95: Unique Binary Search Trees II.

Problem summary:
Generate every structurally distinct binary search tree containing the values
1 through ``n`` exactly once.

Source: https://leetcode.com/problems/unique-binary-search-trees-ii/
"""

from functools import cache
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def build(start: int, end: int) -> tuple[Optional[TreeNode], ...]:
            if start > end:
                return (None,)

            trees: List[Optional[TreeNode]] = []
            for root_value in range(start, end + 1):
                for left in build(start, root_value - 1):
                    for right in build(root_value + 1, end):
                        trees.append(TreeNode(root_value, left, right))
            return tuple(trees)

        return list(build(1, n)) if n else []


def serialize(root: Optional[TreeNode]) -> tuple:
    if root is None:
        return (None,)
    return (root.val, serialize(root.left), serialize(root.right))


if __name__ == "__main__":
    solution = Solution()
    trees = solution.generateTrees(3)
    assert len(trees) == 5
    assert len({serialize(tree) for tree in trees}) == 5
    assert len(solution.generateTrees(1)) == 1
    print("All tests passed.")

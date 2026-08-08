"""LeetCode 107: Binary Tree Level Order Traversal II.

Problem summary:
Return the values of a binary tree grouped by depth, ordered from the deepest
level up to the root and from left to right inside each level.

Source: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

from collections import deque
from typing import Optional


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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        levels: deque[list[int]] = deque()
        queue = deque([root])

        while queue:
            level: list[int] = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            levels.appendleft(level)

        return list(levels)


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution.levelOrderBottom(root) == [[15, 7], [9, 20], [3]]
    assert solution.levelOrderBottom(TreeNode(1)) == [[1]]
    assert solution.levelOrderBottom(None) == []
    print("All tests passed.")

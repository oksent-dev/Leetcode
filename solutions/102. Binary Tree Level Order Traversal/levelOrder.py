"""LeetCode 102: Binary Tree Level Order Traversal.

Problem summary:
Return the values of a binary tree one depth at a time, visiting nodes from
left to right within each level.

Source: https://leetcode.com/problems/binary-tree-level-order-traversal/
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
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        result: list[list[int]] = []
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
            result.append(level)

        return result


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution.levelOrder(root) == [[3], [9, 20], [15, 7]]
    assert solution.levelOrder(TreeNode(1)) == [[1]]
    assert solution.levelOrder(None) == []
    print("All tests passed.")

"""LeetCode 111: Minimum Depth of Binary Tree.

Problem summary:
Return the number of nodes on the shortest path from the root to any leaf.
An empty tree has depth zero.

Source: https://leetcode.com/problems/minimum-depth-of-binary-tree/
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))

        return 0


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution.minDepth(root) == 2

    chain = TreeNode(2, None, TreeNode(3, None, TreeNode(4)))
    assert solution.minDepth(chain) == 3
    assert solution.minDepth(None) == 0
    print("All tests passed.")

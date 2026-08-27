"""LeetCode 124: Binary Tree Maximum Path Sum.

Problem summary:
Return the largest sum of a non-empty path in a binary tree. A path follows
edges without repeating nodes and does not need to include the root.

Source: https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        best = root.val
        downward_gain: dict[TreeNode, int] = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue

            left_gain = max(downward_gain.get(node.left, 0), 0)
            right_gain = max(downward_gain.get(node.right, 0), 0)
            best = max(best, node.val + left_gain + right_gain)
            downward_gain[node] = node.val + max(left_gain, right_gain)

        return best


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6

    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution.maxPathSum(root) == 42
    assert solution.maxPathSum(TreeNode(-3)) == -3
    print("All tests passed.")

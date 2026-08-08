"""LeetCode 110: Balanced Binary Tree.

Problem summary:
Determine whether every node in a binary tree has left and right subtree
heights that differ by at most one.

Source: https://leetcode.com/problems/balanced-binary-tree/
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        heights: dict[TreeNode, int] = {}
        stack: list[tuple[TreeNode, bool]] = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue

            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            if abs(left_height - right_height) > 1:
                return False
            heights[node] = max(left_height, right_height) + 1

        return True


if __name__ == "__main__":
    solution = Solution()
    balanced = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution.isBalanced(balanced)

    unbalanced = TreeNode(
        1,
        TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
        TreeNode(2),
    )
    assert not solution.isBalanced(unbalanced)
    assert solution.isBalanced(None)
    print("All tests passed.")

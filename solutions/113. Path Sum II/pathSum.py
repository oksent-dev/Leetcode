"""LeetCode 113: Path Sum II.

Problem summary:
Return every root-to-leaf path whose node values add up to ``targetSum``.
Each result is represented by its sequence of values.

Source: https://leetcode.com/problems/path-sum-ii/
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        if root is None:
            return []

        result: list[list[int]] = []
        path: list[int] = []
        stack = [(root, targetSum, False)]

        while stack:
            node, remaining, exiting = stack.pop()
            if exiting:
                path.pop()
                continue

            path.append(node.val)
            remaining -= node.val
            stack.append((node, remaining, True))

            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path.copy())
                continue

            if node.right is not None:
                stack.append((node.right, remaining, False))
            if node.left is not None:
                stack.append((node.left, remaining, False))

        return result


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(
        5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
    )
    assert solution.pathSum(root, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert solution.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5) == []
    assert solution.pathSum(None, 0) == []
    print("All tests passed.")

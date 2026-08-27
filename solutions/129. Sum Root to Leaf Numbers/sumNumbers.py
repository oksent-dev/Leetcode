"""LeetCode 129: Sum Root to Leaf Numbers.

Problem summary:
Treat the digits along each root-to-leaf path as one base-10 number and
return the sum of all numbers represented by the tree.

Source: https://leetcode.com/problems/sum-root-to-leaf-numbers/
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        total = 0
        stack = [(root, 0)]

        while stack:
            node, prefix = stack.pop()
            number = prefix * 10 + node.val
            if node.left is None and node.right is None:
                total += number
                continue
            if node.right is not None:
                stack.append((node.right, number))
            if node.left is not None:
                stack.append((node.left, number))

        return total


if __name__ == "__main__":
    solution = Solution()
    assert solution.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25
    root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    assert solution.sumNumbers(root) == 1026
    assert solution.sumNumbers(TreeNode(0)) == 0
    print("All tests passed.")

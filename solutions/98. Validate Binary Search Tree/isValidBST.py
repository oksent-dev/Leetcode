"""LeetCode 98: Validate Binary Search Tree.

Problem summary:
Determine whether every node in a binary tree satisfies the strict binary
search tree ordering rule for its entire left and right subtrees.

Source: https://leetcode.com/problems/validate-binary-search-tree/
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack: list[TreeNode] = []
        previous_value: Optional[int] = None
        current = root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if previous_value is not None and current.val <= previous_value:
                return False
            previous_value = current.val
            current = current.right

        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert not solution.isValidBST(invalid)
    assert not solution.isValidBST(TreeNode(1, TreeNode(1)))
    print("All tests passed.")

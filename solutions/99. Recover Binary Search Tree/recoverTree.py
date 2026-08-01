"""LeetCode 99: Recover Binary Search Tree.

Problem summary:
Exactly two values in a binary search tree were exchanged. Restore the BST in
place without changing its structure. This implementation uses Morris inorder
traversal and O(1) auxiliary space.

Source: https://leetcode.com/problems/recover-binary-search-tree/
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = previous = None
        current = root

        def visit(node: TreeNode) -> None:
            nonlocal first, second, previous
            if previous is not None and previous.val > node.val:
                if first is None:
                    first = previous
                second = node
            previous = node

        while current is not None:
            if current.left is None:
                visit(current)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right is not None and predecessor.right is not current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    visit(current)
                    current = current.right

        if first is not None and second is not None:
            first.val, second.val = second.val, first.val


def inorder(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    solution = Solution()

    first_tree = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    solution.recoverTree(first_tree)
    assert inorder(first_tree) == [1, 2, 3]

    second_tree = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
    solution.recoverTree(second_tree)
    assert inorder(second_tree) == [1, 2, 3, 4]
    print("All tests passed.")

"""LeetCode 109: Convert Sorted List to Binary Search Tree.

Problem summary:
Convert an ascending singly linked list into a height-balanced binary search
tree containing the same values.

Source: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next

        current = head

        def build(size: int) -> Optional[TreeNode]:
            nonlocal current
            if size == 0:
                return None

            left = build(size // 2)
            root = TreeNode(current.val, left)
            current = current.next
            root.right = build(size - size // 2 - 1)
            return root

        return build(length)


def linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def inorder(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def height_or_unbalanced(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left_height = height_or_unbalanced(root.left)
    right_height = height_or_unbalanced(root.right)
    if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1


if __name__ == "__main__":
    solution = Solution()
    values = [-10, -3, 0, 5, 9]
    tree = solution.sortedListToBST(linked_list(values))
    assert inorder(tree) == values
    assert height_or_unbalanced(tree) >= 0
    assert solution.sortedListToBST(None) is None
    print("All tests passed.")

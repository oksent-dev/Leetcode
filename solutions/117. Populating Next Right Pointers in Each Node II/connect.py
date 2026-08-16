"""LeetCode 117: Populating Next Right Pointers in Each Node II.

Problem summary:
For an arbitrary binary tree, connect every node to its immediate neighbor on
the same level, using ``None`` when no such neighbor exists.

Source: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""

from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        current = root

        while current is not None:
            dummy = Node()
            tail = dummy

            while current is not None:
                if current.left is not None:
                    tail.next = current.left
                    tail = tail.next
                if current.right is not None:
                    tail.next = current.right
                    tail = tail.next
                current = current.next

            tail.next = None
            current = dummy.next

        return root


def values_by_next(root: Optional[Node]) -> list[list[int]]:
    result: list[list[int]] = []
    leftmost = root
    while leftmost is not None:
        level: list[int] = []
        next_leftmost = None
        current = leftmost
        while current is not None:
            level.append(current.val)
            if next_leftmost is None:
                next_leftmost = current.left or current.right
            current = current.next
        result.append(level)
        leftmost = next_leftmost
    return result


if __name__ == "__main__":
    solution = Solution()
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    assert solution.connect(root) is root
    assert values_by_next(root) == [[1], [2, 3], [4, 5, 7]]
    assert root.next is None and root.right.next is None and root.right.right.next is None
    assert solution.connect(None) is None
    print("All tests passed.")

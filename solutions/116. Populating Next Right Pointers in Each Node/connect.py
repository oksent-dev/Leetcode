"""LeetCode 116: Populating Next Right Pointers in Each Node.

Problem summary:
In a perfect binary tree, point every node's ``next`` field to the node
immediately to its right on the same level, or to ``None`` at the boundary.

Source: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
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
        leftmost = root

        while leftmost is not None and leftmost.left is not None:
            current = leftmost
            while current is not None:
                current.left.next = current.right
                if current.next is not None:
                    current.right.next = current.next.left
                current = current.next
            leftmost = leftmost.left

        return root


def values_by_next(root: Optional[Node]) -> list[list[int]]:
    result: list[list[int]] = []
    leftmost = root
    while leftmost is not None:
        level: list[int] = []
        current = leftmost
        while current is not None:
            level.append(current.val)
            current = current.next
        result.append(level)
        leftmost = leftmost.left
    return result


if __name__ == "__main__":
    solution = Solution()
    root = Node(
        1,
        Node(2, Node(4), Node(5)),
        Node(3, Node(6), Node(7)),
    )
    assert solution.connect(root) is root
    assert values_by_next(root) == [[1], [2, 3], [4, 5, 6, 7]]
    assert root.next is None and root.right.next is None
    assert solution.connect(None) is None
    print("All tests passed.")

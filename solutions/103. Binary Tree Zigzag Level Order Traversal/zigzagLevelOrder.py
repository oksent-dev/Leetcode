"""LeetCode 103: Binary Tree Zigzag Level Order Traversal.

Problem summary:
Return a binary tree level by level, alternating the value order between
left-to-right and right-to-left on successive levels.

Source: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        result: list[list[int]] = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level: deque[int] = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            result.append(list(level))
            left_to_right = not left_to_right

        return result


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution.zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]
    assert solution.zigzagLevelOrder(TreeNode(1)) == [[1]]
    assert solution.zigzagLevelOrder(None) == []
    print("All tests passed.")

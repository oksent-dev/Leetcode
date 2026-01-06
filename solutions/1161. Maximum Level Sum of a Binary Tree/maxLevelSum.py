"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float("-inf")
        max_level = 0
        current_level = 0
        queue = deque([root])

        while queue:
            current_level += 1
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

        return max_level


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    root1 = TreeNode(1)
    root1.left = TreeNode(7)
    root1.right = TreeNode(0)
    root1.left.left = TreeNode(7)
    root1.left.right = TreeNode(-8)
    print(solution.maxLevelSum(root1))  # Output: 2

    # Example 2:
    root2 = TreeNode(989)
    root2.right = TreeNode(10250)
    root2.right.left = TreeNode(98693)
    root2.right.right = TreeNode(-89388)
    root2.right.right.right = TreeNode(-32127)
    print(solution.maxLevelSum(root2))  # Output: 2

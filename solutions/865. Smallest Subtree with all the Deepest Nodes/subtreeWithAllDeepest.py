"""
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, Tuple


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, None

            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)

            if left_depth > right_depth:
                return left_depth + 1, left_subtree
            elif right_depth > left_depth:
                return right_depth + 1, right_subtree
            else:
                return left_depth + 1, node

        return dfs(root)[1]


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    root1 = TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        TreeNode(1, TreeNode(0), TreeNode(8)),
    )
    result1 = solution.subtreeWithAllDeepest(root1)
    print(result1.val)  # Output: 2

    # Example 2:
    root2 = TreeNode(1)
    result2 = solution.subtreeWithAllDeepest(root2)
    print(result2.val)  # Output: 1

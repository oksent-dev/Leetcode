"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge
such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        total_sum = 0
        subtree_sums = []

        # Calculate total sum and store all subtree sums
        def calculate_subtree_sums(node):
            nonlocal total_sum
            if not node:
                return 0
            left_sum = calculate_subtree_sums(node.left)
            right_sum = calculate_subtree_sums(node.right)
            subtree_sum = node.val + left_sum + right_sum
            subtree_sums.append(subtree_sum)
            total_sum += node.val
            return subtree_sum

        calculate_subtree_sums(root)

        # Find the maximum product
        max_product = 0
        for sub_sum in subtree_sums:
            product = sub_sum * (total_sum - sub_sum)
            max_product = max(max_product, product)

        return max_product % MOD


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    print(solution.maxProduct(root1))  # Output: 110

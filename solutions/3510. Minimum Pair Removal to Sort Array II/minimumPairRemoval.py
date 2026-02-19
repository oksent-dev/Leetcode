"""
Given an array nums, you can perform the following operation any number of times:

- Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
- Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
"""

from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        class Node:
            def __init__(self, val, idx):
                self.val = val
                self.idx = idx
                self.prev = None
                self.next = None
                self.removed = False

        nodes = [Node(x, i) for i, x in enumerate(nums)]
        for i in range(n):
            if i > 0:
                nodes[i].prev = nodes[i - 1]
            if i < n - 1:
                nodes[i].next = nodes[i + 1]

        bad_count = 0
        for i in range(n - 1):
            if nodes[i].val > nodes[i + 1].val:
                bad_count += 1

        if bad_count == 0:
            return 0

        # Heap of (sum, left_index, left_node, right_node)
        # Using left_node.idx for tie-breaking "leftmost"
        h = []
        for i in range(n - 1):
            h.append(
                (
                    nodes[i].val + nodes[i + 1].val,
                    nodes[i].idx,
                    nodes[i + 1].idx,
                    nodes[i],
                    nodes[i + 1],
                )
            )
        heapify(h)

        ops = 0
        while h:
            s, _, _, left, right = heappop(h)

            # Check if this pair is still valid, adjacent, and the sum hasn't changed
            if (
                left.removed
                or right.removed
                or left.next != right
                or s != left.val + right.val
            ):
                continue

            # Perform merge
            ops += 1

            # Neighbors: prev_node -> left -> right -> next_node
            prev_node = left.prev
            next_node = right.next

            # Remove badness contributions from affected pairs
            if prev_node:
                if prev_node.val > left.val:
                    bad_count -= 1
            if left.val > right.val:
                bad_count -= 1
            if next_node:
                if right.val > next_node.val:
                    bad_count -= 1

            # Update left node to be the merged node
            left.val = s
            right.removed = True
            left.next = next_node
            if next_node:
                next_node.prev = left

            # Add badness contributions from new/updated pairs
            if prev_node:
                if prev_node.val > left.val:
                    bad_count += 1
            if next_node:
                if left.val > next_node.val:
                    bad_count += 1

            if bad_count == 0:
                return ops

            # Push potential new pairs to heap
            if prev_node:
                # Pair (prev_node, left) changed its sum
                heappush(
                    h,
                    (
                        prev_node.val + left.val,
                        prev_node.idx,
                        left.idx,
                        prev_node,
                        left,
                    ),
                )
            if next_node:
                # Pair (left, next_node) is new or changed its sum
                heappush(
                    h,
                    (
                        left.val + next_node.val,
                        left.idx,
                        next_node.idx,
                        left,
                        next_node,
                    ),
                )

        return ops


# Test cases:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [5, 2, 3, 1]
    print(sol.minimumPairRemoval(nums1))  # Output: 2

    nums2 = [1, 2, 2]
    print(sol.minimumPairRemoval(nums2))  # Output: 0

    nums3 = [2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1]
    print(sol.minimumPairRemoval(nums3))  # Output: 9

    nums4 = [0, -1, -1, -1, 1, 0, -1]
    print(sol.minimumPairRemoval(nums4))  # Output: 5

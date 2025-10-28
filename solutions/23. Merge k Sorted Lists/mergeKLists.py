"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

from typing import List, Optional

import heapq
import itertools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        counter = itertools.count()

        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, next(counter), l))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, next(counter), node.next))

        return dummy.next


# Test cases
def print_list(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]

solution = Solution()
merged_head = solution.mergeKLists(lists)
print("Merged list:")
print_list(merged_head)  # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None

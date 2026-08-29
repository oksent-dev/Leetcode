"""LeetCode 133: Clone Graph.

Problem summary:
Given one node of a connected undirected graph, return a deep copy containing
new nodes and the same values and neighbor relationships.

Source: https://leetcode.com/problems/clone-graph/
"""

from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        copies = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            original = queue.popleft()
            for neighbor in original.neighbors:
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                copies[original].neighbors.append(copies[neighbor])

        return copies[node]


def adjacency(node: Optional[Node]) -> dict[int, list[int]]:
    if node is None:
        return {}
    result: dict[int, list[int]] = {}
    queue = deque([node])
    visited = {node}
    while queue:
        current = queue.popleft()
        result[current.val] = [neighbor.val for neighbor in current.neighbors]
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


if __name__ == "__main__":
    nodes = [Node(value) for value in range(1, 5)]
    nodes[0].neighbors = [nodes[1], nodes[3]]
    nodes[1].neighbors = [nodes[0], nodes[2]]
    nodes[2].neighbors = [nodes[1], nodes[3]]
    nodes[3].neighbors = [nodes[0], nodes[2]]

    clone = Solution().cloneGraph(nodes[0])
    assert adjacency(clone) == adjacency(nodes[0])
    assert clone is not nodes[0]
    assert all(neighbor not in nodes for neighbor in clone.neighbors)
    assert Solution().cloneGraph(None) is None
    print("All tests passed.")

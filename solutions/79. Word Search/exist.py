"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


# Test cases:
if __name__ == "__main__":
    sol = Solution()

    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1 = "ABCCED"
    print(sol.exist(board1, word1))  # Output: True

    board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word2 = "SEE"
    print(sol.exist(board2, word2))  # Output: True

    board3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word3 = "ABCB"
    print(sol.exist(board3, word3))  # Output: False

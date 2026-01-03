"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int, cols: set, diag1: set, diag2: set) -> int:
            if row == n:
                return 1  # Found a valid arrangement

            count = 0
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # Position is under attack

                # Place the queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Recur to place the next queen
                count += backtrack(row + 1, cols, diag1, diag2)

                # Remove the queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return count

        return backtrack(0, set(), set(), set())


# Test cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.totalNQueens(4))  # Output: 2
    print(solution.totalNQueens(1))  # Output: 1

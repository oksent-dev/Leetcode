"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        min_penalty = float("inf")
        best_hour = 0
        current_penalty = 0

        for j in range(n + 1):
            if j > 0:
                if customers[j - 1] == "Y":
                    current_penalty -= 1
                else:
                    current_penalty += 1

            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_hour = j

        return best_hour


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    customers1 = "YYNY"
    print(solution.bestClosingTime(customers1))  # Output: 2

    customers2 = "NNNNN"
    print(solution.bestClosingTime(customers2))  # Output: 0

    customers3 = "YYYY"
    print(solution.bestClosingTime(customers3))  # Output: 4

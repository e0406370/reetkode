"""
  LCE 1672. Richest Customer Wealth

  You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
  Return the wealth that the richest customer has.

  A customer's wealth is the amount of money they have in all their bank accounts.
  The richest customer is the customer that has the maximum wealth.

  Constraints:
  - m == accounts.length
  - n == accounts[i].length
  - 1 <= m, n <= 50
  - 1 <= accounts[i][j] <= 100

  Topics:
  - Array
  - Matrix
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)


# Time Complexity: O(n^2) - 0 ms -> 100.00%
# Space Complexity: O(1) - 18.08 MB -> 14.66%

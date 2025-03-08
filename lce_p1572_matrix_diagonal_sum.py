"""
  LCE 1572. Matrix Diagonal Sum

  Given a square matrix mat, return the sum of the matrix diagonals.

  Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

  Constraints:
  - n == mat.length == mat[i].length
  - 1 <= n <= 100
  - 1 <= mat[i][j] <= 100

  Topics:
  - Array
  - Matrix
"""


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        pri_diag = 0
        sec_diag = 0
        n = len(mat)

        for i in range(n):
            pri_diag += mat[i][i]
            sec_diag += mat[i][n - 1 - i]

        sec_diag -= mat[n // 2][n // 2] if n % 2 != 0 else 0
        return pri_diag + sec_diag


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 18.10 MB -> 90.69%

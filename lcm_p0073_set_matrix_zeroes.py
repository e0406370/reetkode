"""
  LCM 73. Set Matrix Zeroes

  Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

  You must do it in place.

  Constraints:
  - m == matrix.length
  - n == matrix[0].length
  - 1 <= m, n <= 200
  - -2^31 <= matrix[i][j] <= 2^31 - 1

  Topics:
  - Array
  - Hash Table
  - Matrix
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_set = set()
        col_set = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row_set:
                    matrix[i][j] = 0

                if j in col_set:
                    matrix[i][j] = 0


# Time Complexity: O(m * n) - 0 ms -> 100.00%
# Space Complexity: O(m + n) - 18.43 MB -> 55.50%
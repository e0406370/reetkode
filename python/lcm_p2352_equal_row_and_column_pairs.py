"""
LCM 2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 10^5

Topics:
- Array
- Hash Table
- Matrix
- Simulation
"""


class Solution:

    # Time Complexity: O(n^2) - 38 ms -> 48.32%
    # Space Complexity: O(n) - 21.98 MB -> 59.81%
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_map = {}
        for row in grid:
            row = str(row)
            row_map.setdefault(row, 0)
            row_map[row] += 1

        col_map = {}
        for i in range(n):
            col = []

            for j in range(n):
                col.append(grid[j][i])

            col = str(col)
            col_map.setdefault(col, 0)
            col_map[col] += 1

        return sum(row_map[row] * col_map[row] for row in row_map if row in col_map)

    # Time Complexity: O(n^2) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 22.12 MB -> 19.15%
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_tuples = map(tuple, grid)
        col_tuples = map(tuple, zip(*grid))

        row_counter = Counter(row_tuples)
        res = 0

        for col in col_tuples:

            # Counter returns 0 if col is NOT a key
            res += row_counter[col]

        return res


"""
  methods:
  1. standard approach to obtain row_map and col_map
  2. using map(tuple, grid) and map(tuple, zip(*grid)) to obtain row_tuples and col_tuples respectively
"""

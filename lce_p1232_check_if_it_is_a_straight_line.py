"""
  LCE 1232. Check If It Is a Straight Line

  You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
  Check if these points make a straight line in the XY plane.

  Constraints:
  - 2 <= coordinates.length <= 1000
  - coordinates[i].length == 2
  - -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
  - coordinates contains no duplicate point.

  Topics:
  - Array
  - Math
  - Geometry
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2: return True

        start_x, start_y = coordinates[0]
        for i in range(2, n):
            curr_x, curr_y = coordinates[i]
            curr_diff_x = curr_x - start_x
            curr_diff_y = curr_y - start_y

            prev_x, prev_y = coordinates[i - 1]
            prev_diff_x = prev_x - start_x
            prev_diff_y = prev_y - start_y

            # curr_grad = curr_diff_y // curr_diff_x
            # prev_grad = prev_diff_y // prev_diff_x
            # check if curr_diff_y * prev_diff_x == curr_diff_x * prev_diff_y
            if curr_diff_y * prev_diff_x != curr_diff_x * prev_diff_y:
                return False

        return True


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 18.22 MB -> 35.01%

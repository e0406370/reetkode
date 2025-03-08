"""
  LCE 657. Robot Return to Origin

  There is a robot starting at the position (0, 0), the origin, on a 2D plane.
  Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

  You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move.
  Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

  Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

  Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. 
  Also, assume that the magnitude of the robot's movement is the same for each move.

  Constraints:
  - 1 <= moves.length <= 2 * 104
  - moves only contains the characters 'U', 'D', 'L' and 'R'.

  Topics:
  - String
  - Simulation
"""


class Solution:

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.79 MB -> 83.57%
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for move in moves:
            if move == "U":
                y += 1

            elif move == "D":
                y -= 1

            elif move == "L":
                x -= 1

            elif move == "R":
                x += 1

        return x == 0 and y == 0

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.79 MB -> 83.57%
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for move in moves:
            match move:
                case "U":
                    y += 1

                case "D":
                    y -= 1

                case "L":
                    x -= 1

                case "R":
                    x += 1

        return x == 0 and y == 0

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.79 MB -> 83.57%
    def judgeCircle(self, moves: str) -> bool:
      return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")


"""
  methods:
  1. standard if/elif structure
  2. match and case alternative
  3. count L == count R and count U == count D
"""

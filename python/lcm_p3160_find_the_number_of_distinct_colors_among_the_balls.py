"""
LCM 3160. Find the Number of Distinct Colors Among the Balls

You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit].
Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y.

After each query, you need to find the number of distinct colors among the balls.
Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

Constraints:
- 1 <= limit <= 10^9
- 1 <= n == queries.length <= 10^5
- queries[i].length == 2
- 0 <= queries[i][0] <= limit
- 1 <= queries[i][1] <= 10^9

Topics:
- Array
- Hash Table
- Simulation
"""


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # k -> ball, v -> existing color
        ball_map = {}

        # k -> color, v -> no. of balls with this color
        color_map = {}

        n = len(queries)
        result = [0] * n

        for i in range(n):
            ball, color = queries[i]

            if ball in ball_map:
                existing_color = ball_map.get(ball)
                color_map[existing_color] -= 1

                if color_map[existing_color] == 0:
                    del color_map[existing_color]

            color_map[color] = color_map.get(color, 0) + 1
            ball_map[ball] = color

            result[i] = len(color_map)

        return result


# Time Complexity: O(n) - 65 ms -> 81.86%
# Space Complexity: O(n) - 63.57 MB -> 27.91%

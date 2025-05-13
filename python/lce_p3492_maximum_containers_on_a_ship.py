"""
LCE 3492. Maximum Containers on a Ship

You are given a positive integer n representing an n x n cargo deck on a ship.
Each cell on the deck can hold one container with a weight of exactly w.

However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum weight capacity, maxWeight.

Return the maximum number of containers that can be loaded onto the ship.

Constraints:
- 1 <= n <= 1000
- 1 <= w <= 1000
- 1 <= maxWeight <= 10^9

Topics:
- Math
"""


class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        total_containers = n * n
        total_weight_poss = total_containers * w
        return total_containers if total_weight_poss <= maxWeight else maxWeight // w


# Time Complexity: O(1) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.73 MB -> 59.86%

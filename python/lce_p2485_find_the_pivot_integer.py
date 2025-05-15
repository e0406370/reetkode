"""
LCE 2485. Find the Pivot Integer

Given a positive integer n, find the pivot integer x such that:
- The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

Return the pivot integer x.
If no such integer exists, return -1.
It is guaranteed that there will be at most one pivot index for the given input.

Constraints:
- 1 <= n <= 1000

Topics:
- Math
- Prefix Sum
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        prefix_sum = 0

        for i in range(1, n + 1):
            prefix_sum += i

            threshold = total_sum - prefix_sum + i
            if prefix_sum == threshold:
                return i
            elif prefix_sum > threshold:
                return -1

        return -1


# Time Complexity: O(n) - 7 ms -> 70.41%
# Space Complexity: O(1) - 17.90 MB -> 17.72%

"""
LCE 2769. Find the Maximum Achievable Number

Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.

Constraints:
- 1 <= num, t <= 50

Topics:
- Math
"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


# Time Complexity: O(1) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.70 MB -> 50.83%

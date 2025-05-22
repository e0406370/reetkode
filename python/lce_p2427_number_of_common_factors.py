"""
LCE 2427. Number of Common Factors

Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.

Constraints:
- 1 <= a, b <= 1000

Topics:
- Math
- Enumeration
- Number Theory
"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        lesser = a if a < b else b

        return sum(1 for i in range(1, lesser + 1) if a % i == 0 and b % i == 0)


# Time Complexity: O(min(a, b)) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.77 MB -> 69.21%

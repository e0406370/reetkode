"""
LCE 507. Perfect Number

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

Constraints:
- 1 <= nums <= 10^8

Topics:
- Math
"""

import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        divisors = [1]
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                divisors.extend([i, num // i])

        return sum(divisors) == num


# Time Complexity: O(sqrt(n)) - 3 ms -> 84.23%
# Space Complexity: O(1) - 17.90 MB -> 31.83%

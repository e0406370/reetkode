"""
LCE 3536. Maximum Product of Two Digits

You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

Constraints:
- 10 <= n <= 10^9

Topics:
- Math
- Sorting
"""


class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [0] * 10

        while n > 0:
            digit = n % 10
            digits[digit] += 1
            n //= 10

        prod = 1
        i = 9
        ctr = 0

        while ctr < 2 and i >= 0:
            if digits[i] == 0:
                i -= 1
                continue

            prod *= i
            digits[i] -= 1
            ctr += 1

        return prod


# Time Complexity: O(log n) - 3 ms -> 43.72%
# Space Complexity: O(1) - 17.70 MB -> 65.33%

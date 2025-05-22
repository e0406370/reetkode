"""
LCE 509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.

Topics:
- Math
- Dynamic Programming
- Recursion
- Memoization
"""


class Solution:

    fibonacci_cache = {}

    def fib(self, n: int) -> int:

        if n <= 1:
            return n  # F(0), F(1) = 0

        if n in self.fibonacci_cache:
            return self.fibonacci_cache[n]

        nth_fibonacci_number = self.fib(n - 1) + self.fib(n - 2)
        self.fibonacci_cache[n] = nth_fibonacci_number

        return nth_fibonacci_number


# Time Complexity: O(n) - 43 ms -> 44.33%
# Space Complexity: O(n) - 16.42 MB -> 100.00%

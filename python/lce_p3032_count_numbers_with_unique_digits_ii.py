"""
  LCE 3032. Count Numbers With Unique Digits II (Premium)

  Given two positive integers a and b, return the count of numbers having unique digits in the range [a, b] (inclusive).

  Constraints:
  - 1 <= a <= b <= 1000

  Topics:
  - Hash Table
  - Math
  - Dynamic Programming
"""


class Solution:

    # Time Complexity: O(b - a) - 39 ms -> 44.34%
    # Space Complexity: O(1) - 17.64 MB -> 59.28%
    def numberCount(self, a: int, b: int) -> int:
        count = 0
        for i in range(a, b + 1):
            if self.hasUniqueDigits(i):
                count += 1

        return count

    # Time Complexity: O(b - a) - 30 ms -> 81.00%
    # Space Complexity: O(1) - 17.55 MB -> 71.04%
    def numberCountAlt(self, a: int, b: int) -> int:
        count = 0
        for i in range(a, b + 1):
            i = str(i)
            if len(i) == len(set(i)):
                count += 1

        return count

    def hasUniqueDigits(self, num: int) -> bool:
        digits = []
        while num > 0:
            digit = num % 10
            if digit in digits:
                return False

            digits.append(digit)
            num //= 10

        return True


"""
  methods:
  1. extracting digits from each num and check for any duplicates
  2. using set to remove duplicate digits and compare length between w/o set and w/ set
"""

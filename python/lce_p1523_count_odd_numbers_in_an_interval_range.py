"""
  LCE 1523. Count Odd Numbers in an Interval Range

  Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

  Constraints:
  - 0 <= low <= high <= 10^9

  Topics:
  - Math
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low + 1

        if diff % 2 == 0:
            return diff // 2

        else:
            if high % 2 == 0:
                return diff // 2

            else:
                return diff // 2 + 1


# Time Complexity: O(1) - 42 ms -> 23.95%
# Space Complexity: O(1) - 17.67 MB -> 78.08%


# even (high - low + 1 = 4) => low = 1, high = 4 => odd = 1, 3, even = 2, 4
# low is odd, high is even
# no. of even and odd numbers in the range will be equal (diff // 2)

# odd (high - low + 1 = 3) => low = 8, high = 10 => odd = 9, even = 8, 10
# low is even, high is even
# no. of odd is 1 less than that of even (diff // 2)

# odd (high - low + 1 = 5) => low = 3, high = 7 => odd = 3, 5, 7, even = 4, 6
# low is odd, high is odd
# no. of odd is 1 more than that of even (diff // 2 + 1)

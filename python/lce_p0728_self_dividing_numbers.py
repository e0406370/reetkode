"""
  LCE 728. Self Dividing Numbers

  A self-dividing number is a number that is divisible by every digit it contains.
  - For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
  
  A self-dividing number is not allowed to contain the digit zero.

  Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

  Constraints:
  - 1 <= left, right <= 10^4

  Topics:
  - Math
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if self.isSelfDividing(i)]

    # Time Complexity: O(d) - 3 ms -> 96.77%, d => no. of digits in the num
    # Space Complexity: O(1) - 18.02 MB -> 7.95%
    def isSelfDividing(self, num: int) -> bool:
        if num < 10:
            return True

        if num % 10 == 0:
            return False

        n = num
        while n > 0:
            digit = n % 10
            if digit == 0 or num % digit != 0:
                return False

            n //= 10

        return True

    # Time Complexity: O(d) - 7 ms -> 74.75%, d => no. of digits in the num
    # Space Complexity: O(1) - 18.08 MB -> 7.95%
    def isSelfDividingAlt(self, num: int) -> bool:
        num_str = str(num)

        for d in num_str:
            d = ord(d) - ord("0")
            if d == 0 or num % d != 0:
                return False

        return True


"""
  methods:
  1. extract digits then check 1 by 1
  2. convert num to string then check 1 by 1
"""

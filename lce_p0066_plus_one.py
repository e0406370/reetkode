"""
  LCE 283. Move Zeroes

  You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.

  The digits are ordered from most significant to least significant in left-to-right order.
  The large integer does not contain any leading 0's.

  Increment the large integer by one and return the resulting array of digits.

  Constraints:
  - 1 <= digits.length <= 100
  - 0 <= digits[i] <= 9
  - digits does not contain any leading 0's.

  Topics:
  - Array
  - Math
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            else:
                digits[i] = 0

        digits[:0] = [1]
        return digits


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.89 MB -> 31.21%

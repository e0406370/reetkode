"""
  LCE 3151. Special Array I

  An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

  You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

  Constraints:
  - 1 <= nums.length <= 100
  - 1 <= nums[i] <= 100

  Topics:
  - Array
"""


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if self.isParityEqual(nums[i], nums[i + 1]):
                return False

        return True

    # Time Complexity: O(n) - 2 ms -> 27.51%
    # Space Complexity: O(1) - 17.89 MB -> 23.25%
    def isParityEqual(self, num1: int, num2: int) -> bool:
        return (num1 & 1) ^ (num2 & 1) == 0

    # Time Complexity: O(n) - 2 ms -> 27.51%
    # Space Complexity: O(1) - 17.89 MB -> 23.25%
    def isParityEqualAlt(self, num1: int, num2: int) -> bool:
        return num1 % 2 == num2 % 2


# reference for method 1 - isParityEqual (bitwise operations)
# +---+---+-----+-----+
# | A | B | A&B | A^B |
# +---+---+-----+-----+
# | 0 | 0 |  0  |  0  |
# | 1 | 1 |  1  |  0  |
# | 0 | 1 |  0  |  1  |
# | 1 | 0 |  0  |  1  |
# +---+---+-----+-----+

# reference for method 2 - isParityEqualAlt (modulo comparisons)
# +-------+-------+-----+
# |   A   |   B   | T/F |
# +-------+-------+-----+
# | Even  | Even  |  T  |
# | Odd   | Odd   |  T  |
# | Even  | Odd   |  F  |
# | Odd   | Even  |  F  |
# +-------+-------+-----+

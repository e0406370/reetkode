"""
LCE 1822. Sign of the Product of an Array

Implement a function signFunc(x) that returns:

- 1 if x is positive.
- -1 if x is negative.
- 0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).

Constraints:
- 1 <= nums.length <= 1000
- -100 <= nums[i] <= 100

Topics:
- Array
- Math
"""

from math import prod


class Solution:

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.91 MB -> 41.22%
    def arraySign(self, nums: List[int]) -> int:
        is_negative = False

        for num in nums:
            if num < 0:
                is_negative = not is_negative
            elif num == 0:
                return 0

        return -1 if is_negative else 1

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 20.84 MB -> 20.84%
    def arraySign(self, nums: List[int]) -> int:
        product = prod(nums)

        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0


"""
  methods:
  1. product is not necessary, simply check for negative sign or zero at each iteration
  2. retrieve product and check
"""

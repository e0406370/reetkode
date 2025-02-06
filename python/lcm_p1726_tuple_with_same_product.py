"""
  LCE 1726. Tuple with Same Product

  Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d)
  such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.  

  Constraints:
  - 1 <= nums.length <= 1000
  - 1 <= nums[i] <= 10^4
  - All elements in nums are distinct.

  Topics:
  - Array 
  - Hash Table 
  - Counting
"""

import math


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0

        freq_map = {}
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                freq_map[prod] = freq_map.get(prod, 0) + 1

        count = 0
        for f in freq_map.values():
            if f > 1:
                count += 8 * (math.comb(f, 2))

        return count


# Time Complexity: O(n^2) - 3298 ms -> 93.84%
# Space Complexity: O(n^2) - 46.41 MB -> 41.71%

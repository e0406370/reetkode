"""
  LCM 2364. Count Number of Bad Pairs

  You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

  Return the total number of bad pairs in nums.

  Constraints:
  - 1 <= nums.length <= 10^5
  - 1 <= nums[i] <= 10^9

  Topics:
  - Array
  - Hash Table 
  - Math
  - Counting
"""

from collections import Counter
import math


class Solution:
    # Time Complexity: O(n) - 71 ms -> 75.48%
    # Space Complexity: O(n) - 38.99 MB -> 28.81%
    def countBadPairs(self, nums: List[int]) -> int:
        diff_ctr = Counter(n - i for i, n in enumerate(nums))

        good_pairs = sum(math.comb(diff_cnt, 2) for diff_cnt in diff_ctr.values())

        total_pairs = math.comb(len(nums), 2)

        return total_pairs - good_pairs

    # Time Complexity: O(n) - 75 ms -> 66.90%
    # Space Complexity: O(n) - 38.94 MB -> 28.81%
    def countBadPairsAlt(self, nums: List[int]) -> int:
        diff_ctr = Counter(n - i for i, n in enumerate(nums))

        good_pairs = sum(self.getNC2(diff_cnt) for diff_cnt in diff_ctr.values())

        total_pairs = self.getNC2(len(nums))

        return total_pairs - good_pairs

    def getNC2(self, n: int) -> int:
        return n * (n - 1) // 2


"""
  methods:
  1. using in-built math.comb method to retrieve NC2 value
  2. NC2 = n! / (n - 2)! * 2! = n * (n- 1) * (n - 2)! / (n - 2)! * 2 = n * (n - 1) / 2
"""

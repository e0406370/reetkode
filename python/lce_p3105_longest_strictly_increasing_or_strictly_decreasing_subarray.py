"""
  LCE 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

  You are given an array of integers nums. 
  Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

  Constraints:
  - 1 <= nums.length <= 50
  - 1 <= nums[i] <= 50

  Topics:
  - Array
"""


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # each subarray starts with length of 1 unit
        curr_inc = 1
        curr_dec = 1

        long_inc = 0
        long_dec = 0

        # always start with subarray of 1 unit to save time
        for i in range(1, len(nums)):

            # check for strictly increasing subarray
            if nums[i] > nums[i - 1]:
                curr_inc += 1
            else:
                long_inc = max(curr_inc, long_inc)
                curr_inc = 1

            # check for strictly decreasing subarray
            if nums[i] < nums[i - 1]:
                curr_dec += 1
            else:
                long_dec = max(curr_dec, long_dec)
                curr_dec = 1

        long_inc = max(curr_inc, long_inc)
        long_dec = max(curr_dec, long_dec)
        return max(long_inc, long_dec)


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.76 MB -> 47.33%

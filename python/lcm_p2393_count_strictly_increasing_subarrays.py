"""
  LCM 2393. Count Strictly Increasing Subarrays (Premium)

    You are given an array nums consisting of positive integers.

    Return the number of subarrays of nums that are in strictly increasing order.

    A subarray is a contiguous part of an array.

  Constraints:
  - 1 <= nums.length <= 10^5
  - 1 <= nums[i] <= 10^6

  Topics:
  - Array
  - Math
  - Dynamic Programming
"""


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        full_count = 0
        curr_count = 1

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                curr_count += 1
            else:
                full_count += curr_count * (curr_count + 1) // 2
                curr_count = 1

        full_count += curr_count * (curr_count + 1) // 2
        return full_count


# Time Complexity: O(n) - 25 ms -> 82.35%
# Space Complexity: O(1) - 33.18 MB -> 73.53%

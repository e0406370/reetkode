"""
LCE 1800. Maximum Ascending Subarray Sum

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1.
Note that a subarray of size 1 is ascending.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

Topics:
- Array
"""


class Solution:

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.66 MB -> 79.11%
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = nums[0]

        for i in range(1, len(nums)):

            if nums[i] <= nums[i - 1]:
                max_sum = max(curr_sum, max_sum)
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]

        return max(curr_sum, max_sum)

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.96 MB -> 8.49%
    def maxAscendingSumAlt(self, nums: List[int]) -> int:
        maxEnding = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                maxEnding = nums[i]
                continue

            maxEnding = max(maxEnding, maxEnding + nums[i])

            res = max(maxEnding, res)

        return res


"""
  methods:
  1. standard linear expansion
  2. Kadane's Algorithm
"""

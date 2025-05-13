"""
LCE 896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Constraints:
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5

Topics:
- Array
"""


class Solution:

    # Time Complexity: O(n) - 15 ms -> 92.09%
    # Space Complexity: O(1) - 29.26 MB -> 24.11%
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        isIncreasing = nums[0] <= nums[-1]
        for i in range(1, len(nums)):
            if isIncreasing and nums[i] < nums[i - 1]:
                return False
            elif not isIncreasing and nums[i] > nums[i - 1]:
                return False

        return True

    # Time Complexity: O(n) - 8 ms -> 97.61%
    # Space Complexity: O(1) - 28.88 MB -> 91.54%
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = all(nums[i] <= nums[i - 1] for i in range(1, len(nums)))
        isDecreasing = all(nums[i] >= nums[i - 1] for i in range(1, len(nums)))

        return isIncreasing or isDecreasing


"""
  methods:
  1. single pass: assume strictly increasing or decreasing based on first and last elements, then check consistency while iterating.
  2. double pass: check separately if the array is strictly increasing or decreasing. if neither, then it is not monotonic.
"""

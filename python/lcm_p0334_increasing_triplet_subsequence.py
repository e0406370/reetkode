"""
LCM 334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Constraints:
- 1 <= nums.length <= 5 * 10^5
- -2^31 <= nums[i] <= 2^31 - 1

Topics:
- Array
- Greedy
"""


class Solution:

    # Time Complexity: O(n) - 250 ms -> 5.94%
    # Space Complexity: O(n) - 37.29 MB -> 96.73%
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 3:
            return False

        curr_min = nums[0]
        mins = [0] * (n - 2)
        for i in range(1, n - 1, 1):
            mins[i - 1] = curr_min
            curr_min = min(nums[i], curr_min)

        curr_max = nums[n - 1]
        maxs = [0] * (n - 2)
        for i in range(n - 2, 0, -1):
            maxs[i - 1] = curr_max
            curr_max = max(nums[i], curr_max)

        for i in range(1, n - 1, 1):
            if mins[i - 1] < nums[i] < maxs[i - 1]:
                return True

        return False

    # Time Complexity: O(n) - 12 ms -> 84.40%
    # Space Complexity: O(n) - 37.45 MB -> 65.16%
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first = float("inf")  # nums[i]
        second = float("inf")  # nums[j]

        for num in nums:
            if num <= first:
                first = num

            elif num <= second:
                second = num

            else:
                return True

        return False


"""
  methods:
  1. ignore indices at both ends of nums, retrieve left min and right max for each index then check mins[i - 1] < nums[i] < maxs[i - 1]
  2. iterate thru nums and attempt to update nums[i] or nums[j] for each iteration, otherwise nums[k] (hence nums[i] < nums[j] < nums[k]) is found 
"""

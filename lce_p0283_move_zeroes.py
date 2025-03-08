"""
  LCE 283. Move Zeroes

  Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

  Note that you must do this in-place without making a copy of the array.

  Constraints:
  - 1 <= nums.length <= 10^4
  - -2^31 <= nums[i] <= 2^31 - 1

  Topics:
  - Array
  - Two Pointers
"""


class Solution:

    # Time Complexity: O(n) - 3 ms -> 82.07%
    # Space Complexity: O(n) - 18.55 MB -> 98.45%
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n == 1:
            return nums

        res = [x for x in nums if x != 0]
        res.extend([0] * (n - len(res)))

        for i in range(n):
            nums[i] = res[i]

    # Time Complexity: O(n) - 7 ms -> 46.72%
    # Space Complexity: O(1) - 19.06 MB -> 9.67%
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n == 1:
            return nums

        last_seen_non_zero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[last_seen_non_zero], nums[i] = nums[i], nums[last_seen_non_zero]
                last_seen_non_zero += 1


"""
  methods:
  1. filtering for non-zero elements then extend the rest with zeroes
  2. two pointers: 1st ptr tracks the position where the next non-zero element should be placed, 2nd ptr iterates through array.
     when a non-zero element is found, it is moved to the 1st ptr position and eventually zeroes naturally shift to the end of the array.
"""

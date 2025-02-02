"""
  LCE 1752. Check if Array Is Sorted and Rotated

  Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). 
  Otherwise, return false.

  There may be duplicates in the original array.

  Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
  
  Constraints:
  - 1 <= nums.length <= 100
  - 1 <= nums[i] <= 100

  Topics:
  - Array
"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        # check for first "drop"
        drop_idx = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                drop_idx = i
                break

        # array is originally sorted if drop does not exist
        if drop_idx == -1:
            return True

        # array is rotated if i. nums after drop are increasing and ii. first num > last num
        for i in range(drop_idx + 1, n - 1):
            if nums[i] > nums[i + 1]:
                return False

        return nums[0] >= nums[-1]


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.68 MB -> 70.45%

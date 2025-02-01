"""
  LCE 1133. Largest Unique Number (Premium)

  Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

  Constraints:
  - 1 <= nums.length <= 2000
  - 0 <= nums[i] <= 1000

  Topics:
  - Array
  - Hash Table
  - Sorting
"""


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        largest = -1
        for num in freq_map.keys():
            if freq_map.get(num) == 1:
                largest = max(num, largest)

        return largest

    def largestUniqueNumberAlt(self, nums: List[int]) -> int:
        freq_arr = [0] * (max(nums) + 1)
        for num in nums:
            freq_arr[num] += 1

        largest = -1
        for i in range(len(freq_arr)):
            if freq_arr[i] == 1:
                largest = i

        return largest

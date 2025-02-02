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

from collections import Counter


class Solution:

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.82 MB -> 68.48%
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        largest = -1
        for num in freq_map.keys():
            if freq_map.get(num) == 1:
                largest = max(num, largest)

        return largest

    # Time Complexity: O(n) - 3 ms -> 33.07%
    # Space Complexity: O(n) - 17.83 MB -> 68.48%
    def largestUniqueNumberAlt(self, nums: List[int]) -> int:
        freq_arr = [0] * (max(nums) + 1)
        for num in nums:
            freq_arr[num] += 1

        largest = -1
        for i in range(len(freq_arr)):
            if freq_arr[i] == 1:
                largest = i

        return largest

    # Time Complexity: O(n log n) - 4 ms -> 11.54%
    # Space Complexity: O(n) - 17.90 MB -> 68.48%
    def largestUniqueNumberAlt2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        nums.sort(reverse=True)
        ptr = 0

        while ptr < n:
            # curr is the last element or different from the next element
            if (
                ptr == n - 1
                or nums[ptr] != nums[ptr + 1]
            ):
                return nums[ptr]

            # skip duplicates
            while (
                ptr < n - 1
                and nums[ptr] == nums[ptr + 1]
            ):
                ptr += 1

            # move to the next unique number
            ptr += 1

        return -1

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.90 MB -> 47.86%
    def largestUniqueNumberAlt3(self, nums: List[int]) -> int:
        freq_map = Counter(nums)

        return max(
            (num for num, freq in freq_map.items() if freq == 1),
            default=-1
        )


"""
  methods:
  1. frequency map
  2. frequency array
  3. sorted array in reverse order
  4. counter
"""

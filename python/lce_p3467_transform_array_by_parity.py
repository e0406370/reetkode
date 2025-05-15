"""
LCE 3467. Transform Array by Parity

You are given an integer array nums.
Transform nums by performing the following operations in the exact order specified:

1. Replace each even number with 0.
2. Replace each odd numbers with 1.
3. Sort the modified array in non-decreasing order.

Return the resulting array after performing these operations.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 1000

Topics:
- Array
- Sorting
- Counting
"""


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_freq = sum(1 for i in range(n) if nums[i] % 2 == 0)

        for i in range(n):
            nums[i] = 0 if i < even_freq else 1

        return nums


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.71 MB -> 81.69%

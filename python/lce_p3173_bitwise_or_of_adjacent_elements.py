"""
LCE 3173. Bitwise OR of Adjacent Elements (Premium)

Given an array nums of length n, return an array answer of length n - 1 such that answer[i] = nums[i] | nums[i + 1] where | is the bitwise OR operation.

Constraints:
- 2 <= nums.length <= 100
- 0 <= nums[i] <= 100

Topics:
- Array
- Bit Manipulation
"""


class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[i] | nums[i + 1] for i in range(n - 1)]


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.80 MB -> 35.27%

"""
LCE 3512. Minimum Operations to Make Array Sum Divisible by K

You are given an integer array nums and an integer k. You can perform the following operation any number of times:
- Select an index i and replace nums[i] with nums[i] - 1.

Return the minimum number of operations required to make the sum of the array divisible by k.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- 1 <= k <= 100

Topics:
- Array
- Math
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_sum = sum(nums)
        return num_sum % k if num_sum >= k else num_sum


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 54.87 MB -> 17.91%

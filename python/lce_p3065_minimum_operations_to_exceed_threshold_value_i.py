"""
LCE 3065. Minimum Operations to Exceed Threshold Value I

You are given a 0-indexed integer array nums, and an integer k.

In one operation, you can remove one occurrence of the smallest element of nums.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

Constraints:
- 1 <= nums.length <= 50
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9
- The input is generated such that there is at least one index i such that nums[i] >= k.

Topics:
- Array
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0

        while (min_num := min(nums)) < k:
            nums.remove(min_num)
            count += 1

        return count


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.83 MB -> 35.04%

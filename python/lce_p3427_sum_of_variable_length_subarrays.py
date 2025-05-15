"""
LCE 3427. Sum of Variable Length Subarrays

You are given an integer array nums of size n.
For each index i where 0 <= i < n, define a subarray nums[start ... i] where start = max(0, i - nums[i]).

Return the total sum of all elements from the subarray defined for each index in the array.

Constraints:
- 1 <= n == nums.length <= 100
- 1 <= nums[i] <= 1000

Topics:
- Array
- Prefix Sum
"""


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_sum = 0
        prefix_sum_arr = []
        for i in range(n):
            prefix_sum += nums[i] 
            prefix_sum_arr.append(prefix_sum)

        total = 0
        for i in range(n):
            start = max(0, i - nums[i])

            if start == 0:
                total += prefix_sum_arr[i]
            else:
                total += prefix_sum_arr[i] - prefix_sum_arr[start - 1]

        return total


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(n) - 18.02 MB -> 5.38%

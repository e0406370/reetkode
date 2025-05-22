"""
LCE 3550. Smallest Index With Digit Sum Equal to Index

You are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Topics:
- Array
- Math
"""


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            digit_sum = 0

            while nums[i] > 0:
                digit_sum += nums[i] % 10
                nums[i] //= 10

            if digit_sum == i:
                return i

        return -1


# Time Complexity: O(n * d) - 2 ms -> 71.38%
# Space Complexity: O(1) - 18.07 MB -> 16.27%

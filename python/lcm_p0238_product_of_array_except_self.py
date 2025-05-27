"""
LCM 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Topics:
- Array
- Prefix Sum
"""


class Solution:

    # Time Complexity: O(n) - 23 ms -> 63.92%
    # Space Complexity: O(1) - 23.26 MB -> 79.65%
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix_prod = nums[0]
        suffix_prod = nums[n - 1]

        for i in range(1, n):
            res[i] *= prefix_prod
            prefix_prod *= nums[i]

            res[n - i - 1] *= suffix_prod
            suffix_prod *= nums[n - i - 1]

        return res

    # Time Complexity: O(n) - 23 ms -> 63.92%
    # Space Complexity: O(1) - 23.34 MB -> 54.32%
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix_prod = nums[0]
        for i in range(1, n, 1):
            res[i] *= prefix_prod
            prefix_prod *= nums[i]

        suffix_prod = nums[n - 1]
        for i in range(n - 2, -1, -1):
            res[i] *= suffix_prod
            suffix_prod *= nums[i]

        return res


"""
  methods:
  1. retrieve latest prefix product + suffix product at each index, exclude num at curr index => single pass for both pdts
  2. retrieve latest prefix product + suffix product at each index, exclude num at curr index => double pass: one for prefix, other for suffix 
"""

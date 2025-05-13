"""
LCE 3452. Sum of Good Numbers

Given an array of integers nums and an integer k, an element nums[i] is considered good if it is strictly greater than the elements at indices i - k and i + k (if those indices exist).
If neither of these indices exists, nums[i] is still considered good.

Return the sum of all the good elements in the array.

Constraints:
- 2 <= nums.length <= 100
- 1 <= nums[i] <= 1000
- 1 <= k <= floor(nums.length / 2)

Topics:
- Array
"""


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        good_sum = 0
        n = len(nums)

        for i in range(n):
            res = True
            curr = nums[i]

            left_diff = i - k
            if i - k >= 0:
                res *= curr > nums[left_diff]

            right_diff = i + k
            if i + k < n:
                res *= curr > nums[right_diff]

            if res:
                good_sum += curr

        return good_sum


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.76 MB -> 78.70%

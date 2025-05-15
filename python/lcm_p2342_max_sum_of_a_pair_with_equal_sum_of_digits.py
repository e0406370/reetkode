"""
LCM 2342. Max Sum of a Pair With Equal Sum of Digits

You are given a 0-indexed array nums consisting of positive integers.
You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9

Topics:
- Array
- Hash Table
- Sorting
- Heap (Priority Queue)
"""


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_digits_map = {}  # k = sum of digits of nums[i], v = nums[i]
        max_sum = -1

        for i in range(len(nums)):
            sum_digits = self.getDigitSum(nums[i])
            if sum_digits in sum_digits_map:
                max_sum = max(nums[i] + sum_digits_map.get(sum_digits), max_sum)

                if nums[i] > sum_digits_map.get(sum_digits):
                    sum_digits_map[sum_digits] = nums[i]
            else:
                sum_digits_map[sum_digits] = nums[i]

        return max_sum

    def getDigitSum(self, num: int) -> int:
        digits = 0

        while num > 0:
            digits += num % 10
            num //= 10

        return digits


# Time Complexity: O(n) - 287 ms -> 82.60%
# Space Complexity: O(n) - 33.63 MB -> 52.32%

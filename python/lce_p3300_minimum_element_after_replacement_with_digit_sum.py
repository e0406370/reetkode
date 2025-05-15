"""
LCE 3300. Minimum Element After Replacement With Digit Sum

You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 10^4

Topics:
- Array
- Math
"""


class Solution:

    # Time Complexity: O(n) - 3 ms -> 88.00%
    # Space Complexity: O(1) - 17.77 MB -> 63.73%
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            num = str(nums[i])
            digit_sum = 0

            for d in num:
                digit_sum += int(d)

            nums[i] = digit_sum

        return min(nums)

    def getDigitSum(self, num: int) -> int:
        digit_sum = 0

        while num > 0:
            digit_sum += num % 10
            num //= 10

        return digit_sum

    # Time Complexity: O(n * log m) - 3 ms -> 88.80%
    # Space Complexity: O(1) - 17.76 MB -> 63.73%
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)

        return min(self.getDigitSum(nums[i]) for i in range(n))


"""
  methods:
  1. convert each num to str type, then retrieve digit sum by iterating each ch from L -> R
  2. retrieve digit sum by obtaining each digit from the least significant
"""

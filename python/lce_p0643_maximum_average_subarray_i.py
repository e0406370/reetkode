"""
LCE 643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10^-5 will be accepted.

Constraints:
- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

Topics:
- Array
- Sliding Window
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start_ptr = 0
        end_ptr = k - 1
        n = len(nums)

        max_sum = sum(nums[:k])
        temp_sum = max_sum

        while end_ptr < n - 1:
            temp_sum -= nums[start_ptr]
            start_ptr += 1

            end_ptr += 1
            temp_sum += nums[end_ptr]

            # comparing between previous window with max_sum and current window with temp_sum
            max_sum = max(max_sum, temp_sum)

        return max_sum / k


# Time Complexity: O(n) - 92 ms -> 40.66%
# Space Complexity: O(n) - 27.26 MB -> 95.64%

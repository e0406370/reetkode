"""
LCM 1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9

Topics:
- Array
- Hash Table
- Two Pointers
- Sorting
"""


class Solution:

    # Time Complexity: O(n log n) - 522 ms -> 23.96%
    # Space Complexity: O(1) - 29.93 MB -> 63.91%
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        start_ptr = 0
        end_ptr = len(nums) - 1
        res = 0

        while start_ptr < end_ptr:
            pair_sum = nums[start_ptr] + nums[end_ptr]

            if pair_sum < k:
                start_ptr += 1

            elif pair_sum > k:
                end_ptr -= 1

            else:
                res += 1
                start_ptr += 1
                end_ptr -= 1

        return res

    # Time Complexity: O(n) - 520 ms -> 26.42%
    # Space Complexity: O(n) - 30.54 MB -> 35.54%
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1

            else:
                freq_map[num] = 1

        res = 0
        for num in nums:
            other_num = k - num

            if other_num in freq_map:
                if num == other_num and freq_map[num] > 1:
                    res += 1
                    freq_map[num] -= 2

                elif num != other_num and freq_map[num] > 0 and freq_map[other_num] > 0:
                    res += 1
                    freq_map[num] -= 1
                    freq_map[other_num] -= 1

        return res


"""
  methods:
  1. sorting and two-pointers (start_ptr - lowest, end_ptr - highest)
  2. frequency map to check other num and ensure frequency is above threshold
"""

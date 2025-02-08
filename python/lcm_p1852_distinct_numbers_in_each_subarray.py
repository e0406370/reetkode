"""
  LCM 1852. Distinct Numbers in Each Subarray (Premium)

  Given an integer array nums and an integer k, you are asked to construct the array ans of size n-k+1 where ans[i] is the number of distinct numbers in the subarray nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]].

  Return the array ans.

  Constraints:
  - 1 <= k <= nums.length <= 10^5
  - 1 <= nums[i] <= 10^5

  Topics:
  - Array
  - Hash Table
  - Sliding Window
"""


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans_size = n - k + 1
        ans = [0] * ans_size

        start_ptr = 0
        end_ptr = start_ptr + k - 1

        freq_map = {}
        for i in range(start_ptr, end_ptr + 1):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
        ans[0] = len(freq_map)

        for j in range(1, ans_size):
            start_num = nums[start_ptr]
            if start_num in freq_map:
                freq_map[start_num] -= 1
            if freq_map[start_num] == 0:
                freq_map.pop(start_num)
            start_ptr += 1

            end_ptr += 1
            end_num = nums[end_ptr]
            freq_map[end_num] = freq_map.get(end_num, 0) + 1

            ans[j] = len(freq_map)

        return ans


# Time Complexity: O(n) - 884 ms -> 73.31%
# Space Complexity: O(n) - 38.0 MB -> 36.66%

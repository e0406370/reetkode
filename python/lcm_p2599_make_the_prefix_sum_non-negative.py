"""
  LCM 2599. Make the Prefix Sum Non-negative (Premium)

  You are given a 0-indexed integer array nums. You can apply the following operation any number of times:
  - Pick any element from nums and put it at the end of nums.

  The prefix sum array of nums is an array prefix of the same length as nums such that prefix[i] is the sum of all the integers nums[j] where j is in the inclusive range [0, i].

  Return the minimum number of operations such that the prefix sum array does not contain negative integers.
  The test cases are generated such that it is always possible to make the prefix sum array non-negative.
  
  Constraints:
  - 1 <= nums.length <= 10^5
  - -10^9 <= nums[i] <= 10^9

  Topics:
  - Array
  - Greedy
  - Heap (Priority Queue)
"""

import heapq


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        queue = []
        prefix_sum = 0
        count = 0

        for num in nums:
            if num < 0:
                heapq.heappush(queue, num)

            prefix_sum += num

            if prefix_sum < 0:
                prefix_sum -= heapq.heappop(queue)
                count += 1

        return count


# Time Complexity: O(n log n) - 34 ms -> 80.97%
# Space Complexity: O(n) - 34.33 MB -> 30.19%

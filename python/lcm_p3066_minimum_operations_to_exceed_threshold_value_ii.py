"""
LCM 3066. Minimum Operations to Exceed Threshold Value II

You are given a 0-indexed integer array nums, and an integer k.

In one operation, you will:

- Take the two smallest integers x and y in nums.
- Remove x and y from nums.
- Add min(x, y) * 2 + max(x, y) anywhere in the array.

Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

Constraints:
- 2 <= nums.length <= 2 * 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9
- The input is generated such that an answer always exists. That is, there exists some sequence of operations after which all elements of the array are greater than or equal to k.

Topics:
- Array
- Heap (Priority Queue)
- Simulation
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        opr_count = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

            opr_count += 1

        return opr_count


# Time Complexity: O(n log n) - 265 ms -> 27.31%
# Space Complexity: O(n) - 35.58 MB -> 38.24%

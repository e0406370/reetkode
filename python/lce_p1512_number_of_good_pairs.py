"""
LCE 1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

Topics:
- Array
- Hash Table
- Math
- Counting
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_ctr = Counter(num for num in nums)

        return sum(self.getNC2(num_cnt) for num_cnt in num_ctr.values())

    def getNC2(self, n: int) -> int:
        return n * (n - 1) // 2


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(n) - 46.14 MB -> 46.14%

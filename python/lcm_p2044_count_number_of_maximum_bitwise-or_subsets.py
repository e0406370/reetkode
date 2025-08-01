"""
LCM 2044. Count Number of Maximum Bitwise-OR Subsets

Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

Constraints:
- 1 <= nums.length <= 16
- 1 <= nums[i] <= 10^5

Topics:
- Array
- Backtracking
- Bit Manipulation
- Enumeration
"""


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise_or = reduce(lambda x, y: x | y, nums)
        n = len(nums)

        def backtrack(prev: int, start_idx: int) -> int:
            count = 0

            for i in range(start_idx, n):
                curr = prev | nums[i]
                if curr == max_bitwise_or:
                    count += 1

                count += backtrack(curr, i + 1)

            return count

        return backtrack(0, 0)


# Time Complexity: O(2^n) - 271 ms -> 38.30%
# Space Complexity: O(1) - 17.71 MB -> 72.24%

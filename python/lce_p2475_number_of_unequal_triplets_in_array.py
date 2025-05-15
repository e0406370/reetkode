"""
LCE 2475. Number of Unequal Triplets in Array

You are given a 0-indexed array of positive integers nums.

Find the number of triplets (i, j, k) that meet the following conditions:
- 0 <= i < j < k < nums.length
- nums[i], nums[j], and nums[k] are pairwise distinct.
=> In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].

Return the number of triplets that meet the conditions.

Constraints:
- 3 <= nums.length <= 100
- 1 <= nums[i] <= 1000

Topics:
- Array
- Hash Table
- Sorting
"""


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        found = 0
        L = len(nums)

        for i in range(L):
            num_i = nums[i]

            for j in range(i + 1, L):
                num_j = nums[j]

                if num_i == num_j:
                    continue

                for k in range(j + 1, L):
                    num_k = nums[k]

                    if num_i == num_k or num_j == num_k:
                        continue

                    found += 1

        return found


# Time Complexity: O(n^3) - 166 ms -> 76.48%
# Space Complexity: O(1) - 17.79 MB -> 59.33%

"""
LCE 1995. Count Special Quadruplets

Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
- nums[a] + nums[b] + nums[c] == nums[d], and
- a < b < c < d

Constraints:
- 4 <= nums.length <= 50
- 1 <= nums[i] <= 100

Topics:
- Array
- Hash Table
- Enumeration
"""


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        found = 0
        L = len(nums)

        num_map = defaultdict(list[int])
        max_num = 0
        for idx in range(L):
            num_map[nums[idx]].append(idx)
            max_num = max(nums[idx], max_num)

        for i in range(L):
            for j in range(i + 1, L):
                if nums[i] + nums[j] < max_num:

                    for k in range(j + 1, L):
                        comb = nums[i] + nums[j] + nums[k]

                        if comb in num_map:
                            for idx in num_map[comb]:
                                if idx > k:
                                    found += 1

        return found


# Time Complexity: O(n^3) - 51 ms -> 78.49%
# Space Complexity: O(n) - 17.70 MB -> 86.03%

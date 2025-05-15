"""
LCE 3162. Find the Number of Good Pairs I

You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively.
You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

Constraints:
- 1 <= n, m <= 50
- 1 <= nums1[i], nums2[j] <= 50
- 1 <= k <= 50

Topics:
- Array
- Hash Table
"""


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1

        return count


# Time Complexity: O(n^2) - 7 ms -> 39.44%
# Space Complexity: O(1) - 18.06 MB -> 6.98%

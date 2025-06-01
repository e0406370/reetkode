"""
LCE 2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- -1000 <= nums1[i], nums2[i] <= 1000

Topics:
- Array
- Hash Table
"""


class Solution:

    # Time Complexity: O(n + m) - 11 ms -> 36.12%
    # Space Complexity: O(n + m) - 18.13 MB -> 41.26%
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        return [
            list(set([num for num in nums1 if num not in set_nums2])),
            list(set([num for num in nums2 if num not in set_nums1])),
        ]

    # Time Complexity: O(n + m) - 0 ms -> 100.00%
    # Space Complexity: O(n + m) - 18.28 MB -> 21.80%
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        return [
            list(set_nums1.difference(set_nums2)),
            list(set_nums2.difference(set_nums1)),
        ]


"""
  methods:
  1. standard approach
  2. using in-built set.difference() to compute S1 \ S2 and S2 \ S1 
"""

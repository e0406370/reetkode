"""
LCE 28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters.

Topics:
- Two Pointers
- String
- String Matching
"""


class Solution:

    # Time Complexity: O(n) - 1 ms -> 100.00%
    # Space Complexity: O(1) - 18.01 MB -> 10.63%
    def strStr(self, haystack: str, needle: str) -> int:
        ptr_hsk, ptr_ndl = 0, 0
        len_hsk, len_ndl = len(haystack), len(needle)

        while ptr_hsk < len_hsk:
            start = ptr_hsk

            while haystack[ptr_hsk] == needle[ptr_ndl]:
                ptr_hsk += 1
                ptr_ndl += 1

                if ptr_hsk == len_hsk or ptr_ndl == len_ndl:
                    break

            if ptr_ndl == len_ndl:
                return start

            ptr_ndl = 0
            ptr_hsk = start + 1

        return -1

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.88 MB -> 33.05%
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


"""
  methods:
  1. two pointers: one on haystack and another on needle
  2. in-built find(str) method. note that using index(str) will return ValueError instead of -1
"""

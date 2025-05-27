"""
LCE 392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.

Topics:
- Array
- Two Pointers
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s = 0
        ptr_t = 0

        len_s = len(s)
        len_t = len(t)

        while ptr_s < len_s and ptr_t < len_t:
            if t[ptr_t] == s[ptr_s]:
                ptr_s += 1

            ptr_t += 1

        return ptr_s == len_s


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(n) - 17.80 MB -> 66.98%

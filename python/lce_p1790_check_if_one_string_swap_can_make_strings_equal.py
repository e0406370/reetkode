"""
LCE 1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length.
A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Constraints:
- 1 <= s1.length, s2.length <= 100
- s1.length == s2.length
- s1 and s2 consist of only lowercase English letters.

Topics:
- Hash Table
- String
- Sorting
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n = len(s1)

        s1_freq = [0] * 26
        s2_freq = [0] * 26
        for i in range(n):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] += 1
        if s1_freq != s2_freq:
            return False

        count = 0
        for i in range(n):
            if s1[i] != s2[i]:
                count += 1
            if count > 2:
                return False

        return count == 2


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(n) - 17.81 MB -> 28.33%

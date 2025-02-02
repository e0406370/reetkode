"""
  LCE 1180. Count Substrings with Only One Distinct Letter (Premium)

  Given a string s, return the number of substrings that have only one distinct letter.

  Constraints:
  - 1 <= s.length <= 1000
  - s[i] consists of only lowercase English letters.

  Topics:
  - Math
  - String
"""


class Solution:
    def countLetters(self, s: str) -> int:
        n = len(s)
        ptr_start = 0
        ptr_end = 0
        count = 0

        while ptr_start < n:
            if ptr_end == n - 1 or s[ptr_end] != s[ptr_end + 1]:
                count += self.getNumOfSubstrings(ptr_end - ptr_start + 1)
                ptr_end += 1
                ptr_start = ptr_end

            else:
                ptr_end += 1

        return count

    # sum of arithmetic progression
    def getNumOfSubstrings(self, n: int) -> int:
        return n * (n + 1) // 2


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.67 MB -> 70.53%

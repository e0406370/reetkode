"""
  LCM 1910. Remove All Occurrences of a Substring

  Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
  - Find the leftmost occurrence of the substring part and remove it from s.
  
  Return s after removing all occurrences of part.

  A substring is a contiguous sequence of characters in a string.

  Constraints:
  - 1 <= s.length <= 1000
  - 1 <= part.length <= 1000
  - s and part consists of lowercase English letters.

  Topics:
  - String
  - Stack
  - Simulation
"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while s.find(part) != -1:
            occ_first_idx = s.find(part)
            occ_last_idx = occ_first_idx + len(part) - 1

            s = s[:occ_first_idx] + s[occ_last_idx + 1 :]

        return s


# Time Complexity: O(n^2) - 0 ms -> 100.00%
# Space Complexity: O(n) - 17.87 MB -> 53.28%

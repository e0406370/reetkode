"""
  LCE 1119. Remove Vowels from a String (Premium)

  Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

  Constraints:
  - 1 <= s.length <= 1000
  - s consists only of lowercase English letters.

  Topics:
  - String
"""


class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join((ch for ch in s if ch not in ["a", "e", "i", "o", "u"]))

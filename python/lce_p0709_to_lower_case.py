"""
  LCE 709. To Lower Case

  Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

  Constraints:
  - 1 <= s.length <= 100
  - s consists of printable ASCII characters.

  Topics:
  - String
"""


class Solution:
  
    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.61 MB -> 71.58%
    def toLowerCase(self, s: str) -> str:
        return "".join((ch.lower() if ch.isupper() else ch for ch in s))

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.61 MB -> 71.58%
    def toLowerCase(self, s: str) -> str:
        return "".join((chr(ord(ch) + 32) if ch.isupper() else ch for ch in s))

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.65 MB -> 71.58% 
    def toLowerCase(self, s: str) -> str:
        return "".join((chr(ord(ch) + 32) if ord("A") <= ord(ch) <= ord("A") + 25 else ch for ch in s))


"""
  methods:
  1. using in-built lower() and isupper()
  2. using isupper() to check for uppercase, chr() and ord() to convert uppercase to lowercase
  3. using ord() to check for uppercase, chr() and ord() to convert uppercase to lowercase
"""

"""
LCM 151. Reverse Words in a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Constraints:
- 1 <= s.length <= 3 * 105
- s consist of printable ASCII characters.

Topics:
- Two Pointers
- String
"""


class Solution:

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 18.07 MB -> 24.29%
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[i] for i in range(len(words) - 1, -1, -1))

# split() in Python treats consecutive whitespaces as a single separator and removes leading / trailing whitespaces
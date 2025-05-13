"""
LCE 242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Constraints:
- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

Topics:
- Hash Table
- String
- Sorting
"""


class Solution:

    # Time Complexity: O(n) - 7 ms -> 89.75%
    # Space Complexity: O(n) - 18.12 MB -> 25.21%
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

    # Time Complexity: O(n) - 11 ms -> 72.85%
    # Space Complexity: O(n) - 17.65 MB -> 97.43%
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        for i in range(len(s)):
            freq_s[s[i]] += 1
            freq_t[t[i]] += 1

        return freq_s == freq_t

    # Time Complexity: O(n) - 11 ms -> 72.85%
    # Space Complexity: O(n) - 17.86 MB -> 64.17%
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        freq_arr = [0] * 26

        for i in range(n):
            freq_arr[ord(s[i]) - ord("a")] += 1
            freq_arr[ord(t[i]) - ord("a")] -= 1

        for freq in freq_arr:
            if freq != 0:
                return False

        return True

    # Time Complexity: O(n log n) - 16 ms -> 26.19%
    # Space Complexity: O(n) - 18.46 MB -> 19.55%
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


"""
  methods:
  1. Counter
  2. freq defaultdict
  3. freq array
  4. sorting
"""

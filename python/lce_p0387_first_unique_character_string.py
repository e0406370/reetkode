"""
LCE 387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.

Topics:
- Hash Table
- String
- Queue
- Counting
"""


class Solution:

    # Time Complexity: O(n) - 107 ms -> 7.36%
    # Space Complexity: O(n) - 17.22 MB -> 100.00%
    def firstUniqChar(self, s: str) -> int:

        count = {}

        # setting K(char)-V(occurrence) pairs into the count map
        for char in s:
            count[char] = count.get(char, 0) + 1

        # looping thru the indices of the given string
        for i in range(len(s)):
            char = s[i]

            if count[char] == 1:
                return i

        # default fallback case
        return -1

    # Time Complexity: O(n) - 51 ms -> 79.90%
    # Space Complexity: O(n) - 18.09 MB -> 55.31%
    def firstUniqChar(self, s: str) -> int:

        ctr = Counter(s)

        N = len(s)
        for i in range(N):
            if ctr[s[i]] == 1:
                return i

        return -1


"""
  methods:
  1. using traditional dict to count frequency
  2. using counter to count frequency
"""

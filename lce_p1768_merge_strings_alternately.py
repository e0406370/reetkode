"""
  LCE 1768. Merge Strings Alternately

  You are given two strings word1 and word2.

  Merge the strings by adding letters in alternating order, starting with word1.
  If a string is longer than the other, append the additional letters onto the end of the merged string.

  Return the merged string.

  Constraints:
  - 1 <= word1.length, word2.length <= 100
  - word1 and word2 consist of lowercase English letters.

  Topics:
  - Two Pointers
  - String
"""


class Solution:

    # Time Complexity: O(m + n) - 35 ms -> 76.65%
    # Space Complexity: O(m + n) - 17.88 MB -> 33.47%
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        len_w1 = len(word1)
        len_w2 = len(word2)
        len_comb = len(word1) + len(word2)

        for i in range(len_comb):
            if i < len_w1:
                merged.append(word1[i])

            if i < len_w2:
                merged.append(word2[i])

        return "".join(merged)

    # Time Complexity: O(m + n) - 34 ms -> 81.88%
    # Space Complexity: O(m + n) - 17.85 MB -> 33.47%
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        ptr1 = 0
        ptr2 = 0
        limit = len(word1) + len(word2)

        while len(merged) < limit:
            if ptr1 < len(word1):
                merged.append(word1[ptr1])
                ptr1 += 1

            if ptr2 < len(word2):
                merged.append(word2[ptr2])
                ptr2 += 1

        return "".join(merged)


"""
  methods:
  1. single pointer
  2. double pointers
"""

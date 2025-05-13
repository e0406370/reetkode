"""
LCE 3541. Find Most Frequent Vowel and Consonant

You are given a string s consisting of lowercase English letters ('a' to 'z').

Your task is to:
- Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
- Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them.
If there are no vowels or no consonants in the string, consider their frequency as 0.

The frequency of a letter x is the number of times it occurs in the string.

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters only.

Topics:
- Hash Table
- String
- Counting
"""


class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq_arr = [0] * 26
        base_a = ord("a")
        vowels = "aeiou"

        max_vowel_freq = 0
        max_consonant_freq = 0

        for ch in s:
            freq_arr[ord(ch) - base_a] += 1

            if ch in vowels:
                max_vowel_freq = max(max_vowel_freq, freq_arr[ord(ch) - base_a])
            else:
                max_consonant_freq = max(max_consonant_freq, freq_arr[ord(ch) - base_a])

        return max_vowel_freq + max_consonant_freq


# Time Complexity: O(n) - 3 ms -> 68.69%
# Space Complexity: O(1) - 17.91 MB -> 26.86%

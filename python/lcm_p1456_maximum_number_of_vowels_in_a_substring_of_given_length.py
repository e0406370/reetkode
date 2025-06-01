"""
LCM 1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length

Topics:
- String
- Sliding Window
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start_ptr = 0
        end_ptr = k - 1
        n = len(s)

        vowels = "aeiou"
        max_vowels = sum(1 for i in range(start_ptr, end_ptr + 1) if s[i] in vowels)
        temp_vowels = max_vowels

        while end_ptr < n - 1:
            if s[start_ptr] in vowels:
                temp_vowels -= 1
            start_ptr += 1

            end_ptr += 1
            if s[end_ptr] in vowels:
                temp_vowels += 1

            # comparing between previous window with max_vowels and current window with temp_vowels
            max_vowels = max(max_vowels, temp_vowels)

        return max_vowels


# Time Complexity: O(n) - 73 ms -> 72.11%
# Space Complexity: O(n) - 18.25 MB -> 15.93%

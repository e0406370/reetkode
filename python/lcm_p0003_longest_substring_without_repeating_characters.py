"""
LCM 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Constraints:
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

Topics:
- Hash Table
- String
- Sliding Window
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = len(s)
        start = 0
        end = 0

        seen = set()
        curr = 0
        longest = 0

        while end < L:
            end_ch = s[end]
            if end_ch in seen:
                while (start_ch := s[start]) != end_ch:
                    start += 1
                    seen.remove(start_ch)
                start += 1

            else:
                seen.add(end_ch)

            curr = end - start + 1
            longest = max(curr, longest)

            end += 1

        return longest


# Time Complexity: O(n) - 22 ms -> 34.68%
# Space Complexity: O(n) - 17.66 MB -> 96.84%

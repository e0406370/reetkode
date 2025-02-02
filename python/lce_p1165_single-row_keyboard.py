"""
  LCE 1165. Single-Row Keyboard (Premium)

  There is a special keyboard with all keys in a single row.
  Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25).

  Initially, your finger is at index 0.
  To type a character, you have to move your finger to the index of the desired character.
  The time taken to move your finger from index i to index j is |i - j|.

  You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

  Constraints:
  - keyboard.length == 26
  - keyboard contains each English lowercase letter exactly once in some order.
  - 1 <= word.length <= 104
  - word[i] is an English lowercase letter.

  Topics:
  - Hash Table
  - String
"""


class Solution:

    # Time Complexity: O(n) - 12 ms -> 15.41%
    # Space Complexity: O(1) - 17.85 MB -> 35.41%
    def calculateTime(self, keyboard: str, word: str) -> int:
        curr_idx = 0
        time_taken = 0

        for ch in word:
            next_idx = keyboard.find(ch)
            time_taken += abs(next_idx - curr_idx)
            curr_idx = next_idx

        return time_taken

    # Time Complexity: O(n) - 3 ms -> 98.92%
    # Space Complexity: O(n) - 17.86 MB -> 35.41%
    def calculateTimeAlt(self, keyboard: str, word: str) -> int:
        curr_idx = 0
        time_taken = 0

        key_pos = {ch: idx for idx, ch in enumerate(keyboard)}

        for ch in word:
            next_idx = key_pos[ch]
            time_taken += abs(next_idx - curr_idx)
            curr_idx = next_idx

        return time_taken


"""
  methods:
  1. find() to scan keyboard string from left to right => O(n * 26) = O(26n) time complexity, O(1) space complexity
  2. instant dictionary lookup => O(n * 1) = O(n) time complexity, O(n) space complexity
"""

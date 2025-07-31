"""
LCH 1255. Maximum Score Words Formed by Letters

Given a list of words, list of single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively

Constraints:
- 1 <= words.length <= 14
- 1 <= words[i].length <= 15
- 1 <= letters.length <= 100
- letters[i].length == 1
- score.length == 26
- 0 <= score[i] <= 10
- words[i], letters[i] contains only lower case English letters.

Topics:
- Array
- String
- Dynamic Programming 
- Backtracking
- Bit Manipulation 
- Bitmask
"""


class Solution:
    def recurse(self, words: List[str], letter_freq: List[int], score: List[int], start: int, curr_score: int) -> int:
        max_score = curr_score

        for i in range(start, len(words)):
            word = words[i]
            word_letter_freq = [0] * 26
            for ch in word: word_letter_freq[ord(ch) - ord('a')] += 1

            can_create = True
            temp_score = 0
            temp_letter_freq = list(letter_freq)

            for j in range(26):
                if word_letter_freq[j] > temp_letter_freq[j]:
                    can_create = False
                    break

                temp_score += (word_letter_freq[j] * score[j])
                temp_letter_freq[j] -= word_letter_freq[j]

            if can_create:
                max_score = max(max_score, self.recurse(words, temp_letter_freq, score, i + 1, curr_score + temp_score))

        return max_score

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_freq = [0] * 26
        for letter in letters: letter_freq[ord(letter) - ord('a')] += 1

        return self.recurse(words, letter_freq, score, 0, 0)


# Time Complexity: O(n * 2^n) - 11 ms -> 71.76%
# Space Complexity: O(1) - 17.81 MB -> 73.01% 
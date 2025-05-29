"""
LCE 345. Reverse Vowels of a String

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

    # Time Complexity: O(n) - 9 ms -> 70.27%
    # Space Complexity: O(1) - 19.82 MB -> 11.20%
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        res = list(s)
        N = len(s)

        vowels_indices = [i for i in range(N) if s[i] in vowels]
        V = len(vowels_indices)

        for i in range(V // 2):
            start = vowels_indices[i]
            end = vowels_indices[V - 1 - i]

            res[start], res[end] = res[end], res[start]

        return "".join(res)

    # Time Complexity: O(n) - 7 ms -> 90.83%
    # Space Complexity: O(1) - 18.69 MB -> 49.96%
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        res = list(s)

        start_ptr, end_ptr = 0, len(s) - 1

        while start_ptr < end_ptr:
            if res[start_ptr] not in vowels:
                start_ptr += 1

            elif res[end_ptr] not in vowels:
                end_ptr -= 1

            else:
                res[start_ptr], res[end_ptr] = res[end_ptr], res[start_ptr]
                start_ptr += 1
                end_ptr -= 1

        return "".join(res)

    # Time Complexity: O(n) - 3 ms -> 99.79%
    # Space Complexity: O(n) - 18.52 MB -> 69.58%
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        res = list(s)

        start_ptr, end_ptr = 0, len(s) - 1

        while start_ptr < end_ptr:
            while start_ptr < end_ptr and s[start_ptr] not in vowels:
                start_ptr += 1

            while start_ptr < end_ptr and s[end_ptr] not in vowels:
                end_ptr -= 1

            res[start_ptr], res[end_ptr] = res[end_ptr], res[start_ptr]
            start_ptr += 1
            end_ptr -= 1

        return "".join(res)


"""
  methods:
  1. retrieve indices of vowels, swap vowels at each start-end index pair
  2. two pointers (start and end), use if-elif-else structure to either advance ptrs in their respective dirns or swap vowels between ptrs
  3. two pointers (start and end), use internal while loops to advance ptrs in their respective dirns at 1 go until a vowel is present then swap vowels between ptrs
"""

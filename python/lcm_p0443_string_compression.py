"""
LCM 443. String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:
- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Constraints:
- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

Topics:
- Two Pointers
- String
"""


class Solution:

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.83 MB -> 75.45%
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        main_ptr = 0
        store_ptr = 0

        while main_ptr < n:
            curr = chars[main_ptr]
            sub_ptr = main_ptr

            while sub_ptr < n and curr == chars[sub_ptr]:
                sub_ptr += 1

            freq = sub_ptr - main_ptr

            chars[store_ptr] = curr
            store_ptr += 1
            if freq > 1:
                freq = str(freq)

                for d in freq:
                    chars[store_ptr] = d
                    store_ptr += 1

            main_ptr = sub_ptr

        for j in range(store_ptr, n):
            chars.pop()

        return len(chars)

    # Time Complexity: O(n) - 3 ms -> 39.33%
    # Space Complexity: O(n) - 17.92 MB -> 46.69%
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        main_ptr = 0

        res = []

        while main_ptr < n:
            curr = chars[main_ptr]
            sub_ptr = main_ptr

            while sub_ptr < n and curr == chars[sub_ptr]:
                sub_ptr += 1

            freq = sub_ptr - main_ptr

            res.append(curr)
            if freq > 1:
                freq = str(freq)
                for d in freq:
                    res.append(d)

            main_ptr = sub_ptr

        r = len(res)
        for i in range(r):
            chars[i] = res[i]

        for i in range(r, n):
            chars.pop()

        return r


"""
  methods:
  1. modify chars directly then remove extra slots
  2. append to temp array, modify chars based on temp then remove extra slots 
"""

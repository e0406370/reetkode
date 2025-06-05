/*
  LCM 151. Reverse Words in a String

  Given an input string s, reverse the order of the words.

  A word is defined as a sequence of non-space characters.
  The words in s will be separated by at least one space.

  Return a string of the words in reverse order concatenated by a single space.

  Note that s may contain leading or trailing spaces or multiple spaces between two words.
  The returned string should only have a single space separating the words. Do not include any extra spaces.

  Constraints:
  - 1 <= s.length <= 10^4
  - s contains English letters (upper-case and lower-case), digits, and spaces ' '.
  - There is at least one word in s.

  Topics: Two Pointers, String
*/

class Solution {
  public String reverseWords(String s) {

    // note: "\\s+" matches sequence of one or more whitespace characters.
    String[] words = s.trim().split("\\s+");

    reverseArray(words);

    return String.join(" ", words);
  }

  // alternative: use Collections.reverse(List<T>) instead.
  private void reverseArray(String[] words) {

    int n = words.length;

    for (int i = 0; i < n / 2; i++) {
      String temp = words[i];
      words[i] = words[n - i - 1];
      words[n - i - 1] = temp;
    }
  }
}

// Time Complexity: O(L) - 8 ms -> 39.40%
// Space Complexity: O(L) - 42.65 MB -> 94.35%
// L => length of string s
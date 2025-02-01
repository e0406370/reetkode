/*
  LCM 3163. String Compression III

  Given a string word, compress it using the following algorithm:

  Begin with an empty string comp. While word is not empty, use the following operation:
  - Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
  - Append the length of the prefix followed by c to comp.

  Return the string comp.

  Constraints:
  - 1 <= word.length <= 2 * 10^5
  - word consists only of lowercase English letters.

  Topics: 
  - String
*/

class Solution {
  public String compressedString(String word) {

    int n = word.length();
    StringBuilder sb = new StringBuilder();

    int ptr = 0;
    while (ptr < n) {
      int prefixLen = 1;
      char prefixChar = word.charAt(ptr);

      // increment if i. ptr is not at last char, ii. curr char == next char, iii. prefix len of curr char < 9 
      while (ptr + 1 < n && prefixChar == word.charAt(ptr + 1) && prefixLen < 9) {
        prefixLen++;
        ptr++;
      }

      sb.append(prefixLen);
      sb.append(prefixChar);
      ptr++;
    }

    return sb.toString();
  }
}

// Time Complexity: O(n) - 17 ms -> 87.67%
// Space Complexity: O(n) - 45.74 MB -> 59.28%
/*
  LCE 125. Valid Palindrome

  A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
  Alphanumeric characters include letters and numbers.

  Given a string s, return true if it is a palindrome, or false otherwise.

  Constraints:
  - 1 <= s.length <= 2 * 10^5
  - s consists only of printable ASCII characters.

  Topics: Two Pointers, String
*/

class Solution {

  // Time Complexity: O(n) - 1 ms -> 100.00%
  // Space Complexity: O(n) - 43.11 MB -> 69.00%
  public boolean isPalindrome(String s) {

    int startPtr = 0;
    int endPtr = s.length() - 1;

    while (startPtr < endPtr) {

      char startChar = s.charAt(startPtr);
      char endChar = s.charAt(endPtr);

      if (startChar >= 'A' && startChar <= 'Z') startChar = (char) (startChar - 'A' + 'a');
      if (endChar >= 'A' && endChar <= 'Z') endChar = (char) (endChar - 'A' + 'a');

      if (!((startChar >= 'a' && startChar <= 'z') || (startChar >= '0' && startChar <= '9'))) { 
        startPtr++;
        continue;
      }
      else if (!((endChar >= 'a' && endChar <= 'z') || (endChar >= '0' && endChar <= '9'))) {
        endPtr--;
        continue;
      }
      else {
        if (startChar != endChar) {
          return false;
        }

        startPtr++;
        endPtr--;
      }
    }

    return true;
  }

  // Time Complexity: O(n) - 4 ms -> 55.36%
  // Space Complexity: O(n) - 43.68 MB -> 52.39%
  public boolean isPalindrome2(String s) {

    // as per first requirement
    s = getCleanedString(s);

    int n = s.length();

    // case 1: string length 0 ("") or 1 ("a")
    if (n <= 1) {
      return true;
    }

    // case 2: string length 2 ("ab" or "aa")
    if (n == 2) {
      return s.charAt(0) == s.charAt(1);
    }

    // case 3: string length >= 3
    int startPtr = 0;
    int endPtr = n - 1;

    while (startPtr < endPtr) {

      char startChar = s.charAt(startPtr);
      char endChar = s.charAt(endPtr);

      if (startChar != endChar) {
        return false;
      }

      startPtr++;
      endPtr--;
    }

    return true;
  }

  private String getCleanedString(String s) {

    return s.replaceAll("[^a-zA-Z0-9]+", "").toLowerCase();
  }

  private String getCleanedStringII(String s) {

    StringBuilder sb = new StringBuilder();

    for (char ch : s.toCharArray()) {
      if (Character.isDigit(ch)) {
        sb.append(ch);
      }
      if (Character.isLetter(ch)) {
        sb.append(Character.toLowerCase(ch));
      }
    }

    return sb.toString();
  }
}

/*
  methods:
  1. single pass - first skip ch and advance ptrs if it is not alphanumeric for ch at startPtr / endPtr, if both are OK then compare them
  2. double pass - 1st pass - clean the string as per requirements, 2nd pass - check ch at startPtr / endPtr
*/
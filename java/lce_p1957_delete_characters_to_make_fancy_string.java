/*
  LCE 1957. Delete Characters to Make Fancy String

  A fancy string is a string where no three consecutive characters are equal.

  Given a string s, delete the minimum possible number of characters from s to make it fancy.

  Return the final string after the deletion. It can be shown that the answer will always be unique.

  Constraints:
  - 1 <= s.length <= 10^5
  - s consists only of lowercase English letters.

  Topics: 
  - String
*/

class Solution {
  public String makeFancyString(String s) {

    int n = s.length();

    // s has either 1 or 2 chars
    if (n == 1 || n == 2) {
      return s;
    }

    // s has at least 3 chars
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < n - 2; i++) {
      if (s.charAt(i) == s.charAt(i + 1) && s.charAt(i) == s.charAt(i + 2)) {
        continue;
      }

      sb.append(s.charAt(i));
    }
    sb.append(s.charAt(n - 2));
    sb.append(s.charAt(n - 1));
    
    return sb.toString();
  }
}

// Time Complexity: O(n) - 40 ms -> 37.41%
// Space Complexity: O(n) - 45.38 MB -> 89.20%
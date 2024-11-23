/*
  LCM 271. Encode and Decode Strings (Premium)

  Design an algorithm to encode a list of strings to a single string.
  The encoded string is then decoded back to the original list of strings.

  Please implement encode and decode.

  Topics:
  - String
*/

import java.util.ArrayList;
import java.util.List;

class Solution {

  //#region Method 1
  // Time Complexity: O(L)
  // Space Complexity: O(L + n)
  // L = total no. of characters across all strings, n = no. of strings
  public static String encode(List<String> strs) {
    StringBuilder sb = new StringBuilder();

    for (String str : strs) {
      for (int i = 0; i < str.length(); i++) {
        sb.append(str.charAt(i) - 0);
        sb.append("|");
      }
      sb.append("#");
    }

    return sb.toString();
  }

  public static List<String> decode(String str) {
    List<String> strs = new ArrayList<>();
    StringBuilder main = new StringBuilder();
    StringBuilder temp = new StringBuilder();

    for (int i = 0; i < str.length(); i++) {
      char ch = str.charAt(i);

      if (ch == '|') {
        char letter = (char) Integer.parseInt(temp.toString());
        main.append(letter);
        temp.setLength(0);
      } 
      else if (ch == '#') {
        strs.add(main.toString());
        main.setLength(0);
      } 
      else {
        temp.append(ch);
      }
    }

    return strs;
  }
  //#endregion
}

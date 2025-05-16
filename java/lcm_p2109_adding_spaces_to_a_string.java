/*
  LCM 2109. Adding Spaces to a String

  You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added.
  Each space should be inserted before the character at the given index.

  - For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively.
  - Thus, we obtain "Enjoy Your Coffee".
  
  Return the modified string after the spaces have been added.

  Constraints:
  - 1 <= s.length <= 3 * 105
  - s consists only of lowercase and uppercase English letters.
  - 1 <= spaces.length <= 3 * 105
  - 0 <= spaces[i] <= s.length - 1
  - All the values of spaces are strictly increasing.

  Topics:
  - Array
  - Two Pointers
  - String
  - Simulation
*/

class Solution {

  // Time Complexity: O(n + m) - 21 ms -> 88.52%
  // Space Complexity: O(n + m) - 81.15 MB -> 18.94%
  public String addSpaces(String s, int[] spaces) {
    
    StringBuilder sb = new StringBuilder();

    int strLen = s.length();
    int spacesLen = spaces.length;

    int strPtr = 0;
    int spacesPtr = 0;

    while (strPtr < strLen && spacesPtr < spacesLen) {
      if (strPtr == spaces[spacesPtr]) {
        sb.append(" ");
        spacesPtr++;
      }

      sb.append(s.charAt(strPtr));
      strPtr++;
    }
    sb.append(s, strPtr, strLen);

    return sb.toString();
  }
}
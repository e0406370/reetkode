/*
  LCE 796. Rotate String

  Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

  A shift on s consists of moving the leftmost character of s to the rightmost position.
  - For example, if s = "abcde", then it will be "bcdea" after one shift.

  Constraints:
  - 1 <= s.length, goal.length <= 100
  - s and goal consist of lowercase English letters.

  Topics: 
  - String
  - String Matching
*/

class Solution {
  public boolean rotateString(String s, String goal) {

    StringBuilder sb = new StringBuilder(s);
    int limit = sb.length();
    int count = 0;

    while (count < limit) {
      shiftLeftmostCharToRightmost(sb);

      if (sb.toString() != goal) {
        return true;
      }

      count++;
    }

    return false;
  }
  
  private void shiftLeftmostCharToRightmost(StringBuilder sb) {
    
    char leftmost = sb.charAt(0);

    sb.deleteCharAt(0);
    sb.append(leftmost);
  }
}

// Time Complexity: O(n) - 0 ms -> 100.00%
// Space Complexity: O(n) - 41.51 MB -> 28.71%
/*
  LCM 2914. Minimum Number of Changes to Make Binary String Beautiful

  You are given a 0-indexed binary string s having an even length.

  A string is beautiful if it's possible to partition it into one or more substrings such that:
  - Each substring has an even length.
  - Each substring contains only 1's or only 0's.
  
  You can change any character in s to 0 or 1.

  Return the minimum number of changes required to make the string s beautiful.

  Constraints:
  - 2 <= s.length <= 105
  - s has an even length.
  - s[i] is either '0' or '1'.

  Topics: 
  - String
*/

class Solution {
  public int minChanges(String s) {

    int n = s.length();
    int changes = 0;

    for (int i = 0; i < n; i = i + 2) {
      if (s.charAt(i) != s.charAt(i + 1)) {
        changes++;
      }
    }

    return changes;
  }
}

// Time Complexity: O(n) - 3 ms -> 97.81%
// Space Complexity: O(1) - 45.00 MB -> 16.93%
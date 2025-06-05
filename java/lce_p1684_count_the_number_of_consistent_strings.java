/*
  LCE 1684. Count the Number of Consistent Strings

  You are given a string 'allowed' consisting of distinct characters and an array of strings 'words'. 
  A string is consistent if all characters in the string appear in the string 'allowed'.

  Return the number of consistent strings in the array 'words'.

  Constraints:
  - n == nums.length
  - 1 <= n <= 10^4
  - 0 <= nums[i] <= n
  - All the numbers of nums are unique.

  Topics: Array, Hash Table, String, Bit Manipulation, Counting
*/

class Solution {
  public int countConsistentStrings(String allowed, String[] words) {

    boolean[] allowedChars = new boolean[26];
    for (char ch : allowed.toCharArray()) {
      allowedChars[ch - 'a'] = true;
    }

    int count = words.length;
    for (String word : words) {

      for (char ch : word.toCharArray()) {
        if (!allowedChars[ch - 'a']) {
          count--;
          break;
        }
      }
    }

    return count;
  }
}

// Time Complexity: O(n^2) - 6 ms -> 82.59%
// Space Complexity: O(1) - 45.27 MB -> 65.85%
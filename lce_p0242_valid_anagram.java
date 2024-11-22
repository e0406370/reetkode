/*
  LCE 242. Valid Anagram

  Given two strings s and t, return true if t is an anagram of s, and false otherwise.

  Constraints:
  - 1 <= s.length, t.length <= 5 * 10^4
  - s and t consist of lowercase English letters.

  Topics: 
  - Hash Table
  - String
  - Sorting
*/

import java.util.Arrays;

class Solution {

  // Time Complexity: O(n) - 2 ms -> 97.88%
  // Space Complexity: O(1) - 43.0 MB -> 76.06%
  public boolean isAnagram(String s, String t) {

    if (s.length() != t.length()) {
      return false;
    }

    int[] freqS = new int[26];
    int[] freqT = new int[26];

    for (char ch : s.toCharArray()) {
      freqS[ch - 'a']++;
    }
    for (char ch : t.toCharArray()) {
      freqT[ch - 'a']++;
    }

    return Arrays.equals(freqS, freqT);
  }

  // Time Complexity: O(n) - 6 ms -> 44.40%
  // Space Complexity: O(1) - 42.9 MB -> 85.96%
  public boolean isAnagramAlt1(String s, String t) {

    if (s.length() != t.length()) {
      return false;
    }

    int[] freqArr = new int[26];

    for (int i = 0; i < s.length(); i++) {
      freqArr[s.charAt(i) - 'a']++;
      freqArr[t.charAt(i) - 'a']--;
    }

    for (int freq : freqArr) {
      if (freq != 0) {
        return false;
      }
    }

    return true;
  }

  // Time Complexity: O(n log n + m log m) - 4 ms -> 76.24%
  // Space Complexity: O(1) - 44.9 MB -> 13.69%
  public boolean isAnagramAlt2(String s, String t) {

    if (s.length() != t.length()) {
      return false;
    }

    char[] charS = s.toCharArray();
    char[] charT = t.toCharArray();
    Arrays.sort(charS);
    Arrays.sort(charT);
    
    return Arrays.equals(charS, charT);
  }
}

/*
  methods:
  1. frequency array (compares array contents)
  2. frequency array (checks for equilibrium)
  3. sorting (sort then compare array contents)
*/
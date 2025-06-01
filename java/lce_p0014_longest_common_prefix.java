/*
  LCE 14. Longest Common Prefix

  Write a function to find the longest common prefix string amongst an array of strings.

  If there is no common prefix, return an empty string "".

  Constraints:
  - 1 <= strs.length <= 200
  - 0 <= strs[i].length <= 200
  - strs[i] consists of only lowercase English letters if it is non-empty.

  Topics: 
  - String
  - Trie
*/


class Solution {
  public String longestCommonPrefix(String[] strs) {

    String commonPrefix = "";
    String firstWord = strs[0];

    for (int i = 0; i < firstWord.length(); i++) {
      String firstWordPrefix = firstWord.substring(0, i + 1);

      for (int j = 1; j < strs.length; j++) {
        String otherWord = strs[j];

        if (!otherWord.startsWith(firstWordPrefix)) {
          return commonPrefix;
        }
      }

      commonPrefix = firstWordPrefix;
    }

    return commonPrefix;
  }
}

// Time Complexity: O(n * l) - 1 ms -> 64.24%, n => len of strs; l => length of strs[0]
// Space Complexity: O(1) - 41.78 MB -> 43.06%
/*
  LCM 49. Group Anagrams

  Given an array of strings strs, group the anagrams together. You can return the answer in any order.

  Constraints:
  - 1 <= strs.length <= 10^4
  - 0 <= strs[i].length <= 100
  - strs[i] consists of lowercase English letters.

  Topics: 
  - Array
  - Hash Table
  - String
  - Sorting
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {

  private int[] getFreqArr(String str) {
    
    int[] freqArr = new int[26];

    for (char ch : str.toCharArray()) {
      freqArr[ch - 'a']++;
    }

    return freqArr;
  }

  // Time Complexity: O(n * m) - 18 ms -> 22.11%
  // Space Complexity: O(n) - 48.9 MB -> 10.24%
  public List<List<String>> groupAnagrams(String[] strs) {

    Map<String, List<String>> anagMap = new HashMap<>();

    for (String str : strs) {
      String freqStr = Arrays.toString(getFreqArr(str));

      anagMap.putIfAbsent(freqStr, new ArrayList<>());

      anagMap.get(freqStr).add(str);
    }

    return new ArrayList<>(anagMap.values());
  }

  // Time Complexity: O(n * m log m) - 6 ms -> 97.49%
  // Space Complexity: O(n) - 47.9 MB -> 34.69%
  public List<List<String>> groupAnagramsAlt(String[] strs) {

    Map<String, List<String>> anagMap = new HashMap<>();

    for (String str : strs) {
      char[] chars = str.toCharArray();
      Arrays.sort(chars);
      String sortedStr = new String(chars);

      anagMap.putIfAbsent(sortedStr, new ArrayList<>());

      anagMap.get(sortedStr).add(str);
    }

    return new ArrayList<>(anagMap.values());
  }
}

/*
  methods:
  1. hash map with key - string made of frequency arr
  2. hash map with key - string made of sorted chars
*/
/*
  LCE 3014. Minimum Number of Pushes to Type Word I

  You are given a string word containing distinct lowercase English letters.

  Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them.
  For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

  It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
  The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key.
  You need to find the minimum number of times the keys will be pushed to type the string word.

  Return the minimum number of pushes needed to type word after remapping the keys.

  Constraints:
  - 1 <= word.length <= 26
  - word consists of lowercase English letters.
  - All letters in word are distinct.

  Topics: 
  - Math
  - String
  - Greedy
*/

class Solution {
  public int minimumPushes(String word) {

    int n = word.length();

    int keys = 8;
    int pushCtr = 1;
    int pushSum = 0;

    for (int i = 0; i < n; i++) {
      pushSum += pushCtr;
      keys--;

      // all keys have been used for the current push counter
      if (keys == 0) {
        pushCtr++;
        keys = 8;
      }
    }

    return pushSum;
  }
}

// Time Complexity: O(n) - 0 ms -> 100.00%
// Space Complexity: O(1) - 41.57 MB -> 85.98%
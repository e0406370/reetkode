/*
  LCM 3016. Minimum Number of Pushes to Type Word II

  You are given a string word containing lowercase English letters.

  Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them.
  For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

  It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
  The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key.
  You need to find the minimum number of times the keys will be pushed to type the string word.

  Return the minimum number of pushes needed to type word after remapping the keys.

  Constraints:
  - 1 <= word.length <= 10^5
  - word consists of lowercase English letters.

  Topics: 
  - Hash Table 
  - String
  - Greedy 
  - Sorting 
  - Counting
*/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
  public int minimumPushes(String word) {

    Map<Character, Integer> freqMap = new HashMap<>();
    for (char ch : word.toCharArray()) {
      freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
    }

    PriorityQueue<Map.Entry<Character, Integer>> freqQueue = new PriorityQueue<>(
      (e1, e2) -> e2.getValue() - e1.getValue()
    );
    freqQueue.addAll(freqMap.entrySet());

    int slots = 8;
    int pushCtr = 1;
    int pushSum = 0;
    
    while (!freqQueue.isEmpty()) {
      pushSum += (pushCtr * freqQueue.poll().getValue());
      slots--;

      if (slots == 0) {
        pushCtr++;
        slots = 8;
      }
    }

    return pushSum;
  }
}

// Time Complexity: O(n log n) - 65 ms -> 26.42%
// Space Complexity: O(n) - 45.89 MB -> 27.13%
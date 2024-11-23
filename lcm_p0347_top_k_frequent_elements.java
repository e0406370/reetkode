/*
  LCM 347. Top K Frequent Elements

  Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

  Constraints:
  - 1 <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4
  - k is in the range [1, the number of unique elements in the array].
  - It is guaranteed that the answer is unique.

  Topics: 
  - Array
  - Hash Table
  - Divide and Conquer
  - Sorting
  - Heap (Priority Queue)
  - Bucket Sort
  - Counting
  - Quickselect
*/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {

  // Time Complexity: O(n log n) - 13 ms -> 76.11%
  // Space Complexity: O(n) - 48.6 MB -> 52.11%
  public int[] topKFrequent(int[] nums, int k) {
    
    Map<Integer, Integer> freqMap = new HashMap<>();
    for (int num : nums) {
      freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
    }

    PriorityQueue<Map.Entry<Integer, Integer>> queue = new PriorityQueue<>(
      (e1, e2) -> e2.getValue() - e1.getValue()
    );
    queue.addAll(freqMap.entrySet());

    int[] res = new int[k];
    for (int i = 0; i < k; i++) {
      res[i] = queue.poll().getKey();
    }
    
    return res;
  }
}

/*
  methods:
  1. priority queue - decreasing frequency
*/
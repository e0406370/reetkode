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
import java.util.LinkedList;
import java.util.List;
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

  // Time Complexity: O(n) - 12 ms -> 82.75%
  // Space Complexity: O(n) - 50.15 MB -> 5.35%
  @SuppressWarnings("unchecked")
  public int[] topKFrequentAlt(int[] nums, int k) {

    int n = nums.length;

    Map<Integer, Integer> freqMap = new HashMap<>();
    for (int num : nums) {
      freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
    }

    List<Integer>[] buckets = new List[n + 1]; // create (n + 1) buckets; +1 since arrays are zero-indexed
    for (int i = 0; i < n + 1; i++) {
      buckets[i] = new LinkedList<>();
    }

    for (Map.Entry<Integer, Integer> e : freqMap.entrySet()) {
      buckets[e.getValue()].add(e.getKey()); // buckets are categorised by the frequency of the num
    }

    int[] res = new int[k];
    for (int resIdx = 0, buckIdx = n; resIdx < k && buckIdx >= 0; buckIdx--) {
      for (int buck : buckets[buckIdx]) {
        res[resIdx++] = buck;
      }

      if (resIdx == k) {
        return res;
      }
    }

    return res;
  }
}

/*
  methods:
  1. priority queue - decreasing frequency
  2. bucket sort algorithm - only grouping into buckets based on frequency; sorting within each bucket is not required

  note for 2.
  - each element in nums is processed only once, either when added to a bucket or when extracted from it
  - outer loop iterates over the buckets
  - inner loop iterates over the elements in a specific bucket
*/
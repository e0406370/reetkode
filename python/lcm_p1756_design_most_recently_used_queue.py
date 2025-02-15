"""
  LCM 1756. Design Most Recently Used Queue
  
  Design a queue-like data structure that moves the most recently used element to the end of the queue.

  Implement the MRUQueue class:
  - MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
  - int fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.
  
  Constraints:
  - 1 <= n <= 2000
  - 1 <= k <= n
  - At most 2000 calls will be made to fetch.
  
  Topics:
  - Array 
  - Hash Table 
  - Stack 
  - Design 
  - Binary Indexed Tree #
  - Ordered Set
"""


# Time Complexity: O(n) - 2094 ms -> 5.15%
# Space Complexity: O(n) - 19.21 MB -> 26.80%
class MRUQueue:

    def __init__(self, n: int):
        self.idx_map = {idx: num for idx, num in enumerate(list(range(1, n + 1)))}

    def fetch(self, k: int) -> int:
        size = len(self.idx_map)
        if k == size:
            return self.idx_map.get(k - 1)

        fetched = self.idx_map.get(k - 1)

        for i in range(k - 1, size - 1):
            self.idx_map[i] = self.idx_map.get(i + 1)
        self.idx_map[size - 1] = fetched

        return fetched


# Time Complexity: O(n) - 28 ms -> 78.87%
# Space Complexity: O(n) - 18.92 MB -> 78.35%
class MRUQueue:

    def __init__(self, n: int):
        self.queue = [x for x in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        if k == len(self.queue):
            return self.queue[k - 1]

        fetched = self.queue.pop(k - 1)
        self.queue.append(fetched)

        return fetched


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)

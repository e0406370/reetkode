"""
LCM 2349. Design a Number Container System

Design a number container system that can do the following:
- Insert or Replace a number at the given index in the system.
- Return the smallest index for the given number in the system.

Implement the NumberContainers class:
- NumberContainers() Initializes the number container system.
- void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
- int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.

Constraints:
- 1 <= index, number <= 10^9
- At most 10^5 calls will be made in total to change and find.

Topics:
- Hash Table
- Design
- Heap (Priority Queue)
- Ordered Set
"""


class NumberContainers:

    def __init__(self):
        # k -> idx, v -> existing num
        self.containers = {}

        # k -> num, v -> min heap of idx containing this num
        self.numbers = {}

    def change(self, index: int, number: int) -> None:
        self.containers[index] = number

        if number not in self.numbers:
            self.numbers[number] = []
        heapq.heappush(self.numbers[number], index)

    def find(self, number: int) -> int:
        if number not in self.numbers:
            return -1

        while self.numbers[number]:
            smallest_index = self.numbers[number][0]

            if self.containers.get(smallest_index) == number:
                return smallest_index
            else:
                heapq.heappop(self.numbers[number])

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)


# Time Complexity: O(log n) - 102 ms -> 86.27%
# Space Complexity: O(n) - 81.98 MB -> 47.55%

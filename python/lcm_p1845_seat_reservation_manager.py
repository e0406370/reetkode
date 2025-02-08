"""
  LCM 1845. Seat Reservation Manager

  Design a system that manages the reservation state of n seats that are numbered from 1 to n.

  Implement the SeatManager class:

  - SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
  - int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
  - void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

  Constraints:
  - 1 <= n <= 10^5
  - 1 <= seatNumber <= n
  - For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
  - For each call to unreserve, it is guaranteed that seatNumber will be reserved.
  - At most 10^5 calls in total will be made to reserve and unreserve.

  Topics:
  - Design
  - Heap (Priority Queue)
"""

import heapq


class SeatManager:

    def __init__(self, n: int):
        self.seats = [x for x in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

# Time Complexity: O(log n) - 135 ms -> 77.19%
# Space Complexity: O(n) - 46.84 MB -> 53.41%

"""
LCE 2073. Time Needed to Buy Tickets

There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket.
A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets.
If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.

Constraints:
- n == tickets.length
- 1 <= n <= 100
- 1 <= tickets[i] <= 100
- 0 <= k < n

Topics:
- Array
- Queue
- Simulation
"""


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        time_taken = 0

        while True:
            if k == 0 and queue[k] == 1:
                break

            front_person = queue.popleft() - 1
            if front_person != 0:
                queue.append(front_person)

            k -= 1
            if k < 0:
                k = len(queue) - 1

            time_taken += 1

        return time_taken + 1


# Time Complexity: O(n * tickets[k]) - 7 ms -> 52.61%
# Space Complexity: O(n) - 17.74 MB -> 55.80%

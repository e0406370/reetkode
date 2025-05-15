"""
LCM 2391. Minimum Amount of Time to Collect Garbage

You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house.
garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively.
Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage.
Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment.
While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.

Constraints:
- 2 <= garbage.length <= 10^5
- garbage[i] consists of only the letters 'M', 'P', and 'G'.
- 1 <= garbage[i].length <= 10
- travel.length == garbage.length - 1
- 1 <= travel[i] <= 100

Topics:
- Array
- String
- Prefix Sum
"""


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel_prefix = [travel[0]]
        for i in range(1, len(travel)):
            travel_prefix.append(travel[i] + travel_prefix[i - 1])

        glass_mins = 0
        glass_idx = -1

        paper_mins = 0
        paper_idx = -1

        metal_mins = 0
        metal_idx = -1

        for i in range(len(garbage)):
            for ch in garbage[i]:
                match ch:
                    case "G":
                        glass_mins += 1
                        glass_idx = i - 1
                    case "P":
                        paper_mins += 1
                        paper_idx = i - 1
                    case "M":
                        metal_mins += 1
                        metal_idx = i - 1

        glass_mins += travel_prefix[glass_idx] if glass_idx > -1 else 0
        paper_mins += travel_prefix[paper_idx] if paper_idx > -1 else 0
        metal_mins += travel_prefix[metal_idx] if metal_idx > -1 else 0

        return glass_mins + paper_mins + metal_mins


# Time Complexity: O(g + m) - 159 ms -> 38.73%, g - length of garbage list, m - total no. of characters across all strings in garbage
# Space Complexity: O(g) - 17.81 MB -> 35.56%, g - length of garbage list (t = g - 1)

"""
LCM 3527. Find the Most Common Response

You are given a 2D string array responses where each responses[i] is an array of strings representing survey responses from the ith day.

Return the most common response across all days after removing duplicate responses within each responses[i].
If there is a tie, return the lexicographically smallest response.

Constraints:
- 1 <= responses.length <= 1000
- 1 <= responses[i].length <= 1000
- 1 <= responses[i][j].length <= 10
- responses[i][j] consists of only lowercase English letters

Topics:
- Array
- Hash Table
- String
- Counting
"""


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        response_dict = {}

        for response_list in responses:
            response_list = set(response_list)

            for response in response_list:
                if response not in response_dict:
                    response_dict[response] = 0

                response_dict[response] += 1

        return min(response_dict, key=lambda r: (-response_dict[r], r))


# Time Complexity: O(N * L) - 541 ms -> 29.00%, N - no. of lists, L - average length of list
# Space Complexity: O(U) - 165.84 MB -> 69.06%, U - no. of unique responses

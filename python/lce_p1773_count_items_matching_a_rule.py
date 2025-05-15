"""
LCE 1773. Count Items Matching a Rule

You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item.
You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:
- ruleKey == "type" and ruleValue == typei.
- ruleKey == "color" and ruleValue == colori.
- ruleKey == "name" and ruleValue == namei.

Return the number of items that match the given rule.

Constraints:
- 1 <= items.length <= 10^4
- 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
- ruleKey is equal to either "type", "color", or "name".
- All strings consist only of lowercase letters.

Topics:
- Array
- String
"""


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index_map = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        matches = 0

        target_index = index_map[ruleKey]
        for item in items:
            if item[target_index] == ruleValue:
                matches += 1

        return matches


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 22.84 MB -> 53.12%

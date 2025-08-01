"""
LCM 366. Find Leaves of Binary Tree (Premium)

Given the root of a binary tree, collect a tree's nodes as if you were doing this:
- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100

Topics:
- Tree
- Depth-First Search
- Binary Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # group nodes based on the maximum depth of their left and right subtrees
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapper = {}

        def dfs(node: Optional[TreeNode], level: int) -> int:
            if not node:
                return level

            left = dfs(node.left, level)
            right = dfs(node.right, level)
            level = max(left, right)

            if level not in mapper:
                mapper[level] = [node.val]
            else:
                mapper[level].append(node.val)

            return level + 1

        dfs(root, 0)
        return list(mapper.values())


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(n) - 17.28 MB -> 42.81%

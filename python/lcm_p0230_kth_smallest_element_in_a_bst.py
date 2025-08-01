"""
LCM 230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

Topics:
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], arr: list[int]) -> list[int]:
        if node.left:
            self.dfs(node.left, arr)

        arr.append(node.val)

        if node.right:
            self.dfs(node.right, arr)

        return arr

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = self.dfs(root, [])
        return arr[k - 1]


# Time Complexity: O(n) - 4 ms -> 16.15%
# Space Complexity: O(n) - 21.20 MB -> 27.36%

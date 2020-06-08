"""
https://leetcode.com/problems/leaf-similar-trees/
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Constraints:

Both of the given trees will have between 1 and 200 nodes.
Both of the given trees will have values between 0 and 200
"""

# time complexity: O(n), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        from itertools import zip_longest
        return all(x == y for x, y in zip_longest(self.dfs(root1), self.dfs(root2)))

    def dfs(self, root: TreeNode):
        if root.left is None and root.right is None:
            yield root.val

        if root.left is not None:
            yield from self.dfs(root.left)

        if root.right is not None:
            yield from self.dfs(root.right)

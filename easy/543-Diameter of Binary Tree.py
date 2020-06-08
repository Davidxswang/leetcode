"""
https://leetcode.com/problems/diameter-of-binary-tree/
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Thanks to the solution provided by the problem.
# time complexity: O(n), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.long = 1
        self.dfs(root)
        return self.long - 1

    def dfs(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.long = max(self.long, left + right + 1)
        return max(left, right) + 1

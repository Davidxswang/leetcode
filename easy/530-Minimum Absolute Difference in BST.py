"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).


Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""

# Using the left-root-right order to traverse the binary search tree, then all the distance between adjacent elements can tell us which is the smallest.
# time complexity: O(1), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = None
        self.min = None
        self.getmin(root)
        return self.min

    def getmin(self, root: TreeNode) -> None:
        if root is None:
            return
        self.getmin(root.left)
        if self.prev is not None:
            diff = abs(root.val - self.prev)
            self.min = diff if self.min is None or diff < self.min else self.min
        self.prev = root.val
        self.getmin(root.right)

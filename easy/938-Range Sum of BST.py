"""
https://leetcode.com/problems/range-sum-of-bst/
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""

# time complexity: O(n), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        self.L = L
        self.R = R
        self.dfs(root)
        return self.sum

    def dfs(self, root: TreeNode) -> None:
        if root is None:
            return
        if root.val < self.L:
            self.dfs(root.right)
        elif root.val > self.R:
            self.dfs(root.left)
        else:
            self.dfs(root.left)
            self.dfs(root.right)
            self.sum += root.val

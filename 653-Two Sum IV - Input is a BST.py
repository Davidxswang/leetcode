"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

# time complexity: O(n), space complexity: O(1) omitting the call stack storage.
# I used yield to save the extra space in this program.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        left = self.getleftright(root)
        right = self.getrightleft(root)
        i = next(left)
        j = next(right)

        while i is not None and j is not None and i is not j:
            if i + j == k:
                return True
            if i == j:
                return False
            if i + j < k:
                i = next(left)
            else:
                j = next(right)

    def getleftright(self, root: TreeNode) -> int:
        if root is None:
            return
        yield from self.getleftright(root.left)
        yield root.val
        yield from self.getleftright(root.right)

    def getrightleft(self, root: TreeNode) -> int:
        if root is None:
            return
        yield from self.getrightleft(root.right)
        yield root.val
        yield from self.getrightleft(root.left)
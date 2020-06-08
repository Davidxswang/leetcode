"""
https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""

# It's pretty easy.
# time complexity: O(nlogn), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) if root is not None else True

    def height(self, root: TreeNode) -> int:
        return 1 + max(self.height(root.left), self.height(root.right)) if root is not None else 0


# To make the running time shorter, we can only traverse the tree once.
# In this method, we make most of the information we get after we traver one branch of the tree.
# time complexity: O(n), space complexity: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1

    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0

        leftheight = self.height(root.left)
        if leftheight == -1:
            return -1
        rightheight = self.height(root.right)
        if rightheight == -1:
            return -1

        return -1 if abs(leftheight - rightheight) > 1 else 1 + max(leftheight, rightheight)
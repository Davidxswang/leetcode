"""
https://leetcode.com/problems/subtree-of-another-tree/
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.


Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Very good question.
# Thanks to the solution.
# The key idea is to traverse very node in the tree, and treat each node as a root of tree A to see if tree A is equal to t.
# time complexity: O(nm), space complexity: O(depth of s) if recursion is considered, where n and m are the numbers of element in tree s and t.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return t is None
        return self.equal(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def equal(self, root: TreeNode, t: TreeNode) -> bool:
        if root is None and t is None:
            return True

        if root is not None and t is not None and root.val == t.val:
            return self.equal(root.left, t.left) and self.equal(root.right, t.right)

        return False
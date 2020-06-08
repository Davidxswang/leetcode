"""
https://leetcode.com/problems/convert-bst-to-greater-tree/
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""

# right-middle-left order is the most convenient way to calculate the sum of the elements which are larger than the current node.
# time complexity: O(n), space complexity: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.prev = 0
        self.convert(root)
        return root

    def convert(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        self.convert(root.right)
        root.val += self.prev
        self.prev = root.val
        self.convert(root.left)
"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# time complexity: O(n), space complexity: O(n)
# the main idea is to find the root and find how many nodes in its left children and right children, then use these two numbers to segment the preorder list. We do this recursively we can find the final tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
     
        location = dict(zip(inorder, range(len(inorder))))
        
        def helper(pre_start, pre_end, in_start, in_end) -> TreeNode:
            if pre_end == pre_start:
                return TreeNode(preorder[pre_start])
            if pre_start > pre_end:
                return None
            i = location[preorder[pre_start]]
            return TreeNode(preorder[pre_start], helper(pre_start+1, pre_start-in_start+i,in_start, i-1), helper(pre_start-in_start+i+1, pre_end, i+1, in_end))
        
        return helper(0, len(preorder)-1, 0, len(inorder)-1)

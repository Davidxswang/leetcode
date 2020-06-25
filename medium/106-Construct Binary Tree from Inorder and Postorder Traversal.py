"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# time complexity: O(n), space complexity: O(n)
# this is very similar to question 105. The main idea is to locate the root in the inorder list and find the number of nodes in its left and right subtree, then partition preorder list using these two numbers. We do this recursively to reach the final answer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        location = dict(zip(inorder, range(len(inorder))))
        
        def helper(in_start=0, in_end=len(inorder)-1, p_start=0, p_end=len(postorder)-1) -> TreeNode:
            if in_start == in_end:
                return TreeNode(inorder[in_start])
            if in_start > in_end:
                return None
            i = location[postorder[p_end]]
            return TreeNode(postorder[p_end], helper(in_start, i-1, p_start, p_start+i-1-in_start), helper(i+1, in_end, p_end-1-in_end+i+1, p_end-1))
            
        
        return helper()

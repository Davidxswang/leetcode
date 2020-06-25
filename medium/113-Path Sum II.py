"""
https://leetcode.com/problems/path-sum-ii/
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

# time complexity: O(n), space complexity: O(height of the tree) due to the call stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        result = []
        
        def helper(path, node):
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None:
                if sum(path) == target:
                    result.append(list(path))

            helper(path, node.left)
            helper(path, node.right)
            path.pop()
        
        helper([], root)
        return result
                

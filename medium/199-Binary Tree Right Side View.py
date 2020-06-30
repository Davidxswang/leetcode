"""
https://leetcode.com/problems/binary-tree-right-side-view/
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# time complexity: O(n), space complexity: O(height of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        
        def helper(head, layer):
            if head is None:
                return
            if layer == len(result):
                result.append(head.val)
            else:
                result[layer] = head.val
            helper(head.left, layer+1)
            helper(head.right, layer+1)
        
        helper(root, 0)
        
        return result

"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# time complexity: O(n), space complexity: O(n)
# the key is to know when to add a new list to the result to represent a new layer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        result = [[]]
        size = 1
        while queue:
            node = queue.pop(0)
            size -= 1
            if node:
                result[-1].append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if size == 0 and queue:
                result.append([])
                size = len(queue)
                
        if result and not result[-1]:
            result.pop()
        return result

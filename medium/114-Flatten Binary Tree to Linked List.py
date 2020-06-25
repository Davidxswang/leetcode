"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

# time complexity: O(n), space complexity: O(height of the tree)
# this is a very good question. The answer is provided by @tusizi in the discussion area. 
# the main idea is to traverse the tree in postorder and traverse right node first, then left node, then root. So this is totally reverse preorder which is what we want.
# When we finish the right node, we make the right node (and its subtree if there is any) the final structure, then we move on to the left node do the same thing and make always connect each node to the last node we have finish processing.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root, None)
    
    def helper(self, root: TreeNode, pre: TreeNode) -> None:
        if root is None:
            return pre
        pre = self.helper(root.right, pre)
        pre = self.helper(root.left, pre)
        root.left = None
        root.right = pre
        pre = root
        return pre

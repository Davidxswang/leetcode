"""
https://leetcode.com/problems/increasing-order-search-tree/
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

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
            \
             7
              \
               8
                \
                 9


Constraints:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""

# time complexity: O(n), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.newroot = None
        self.current = None
        self.dfs(root)
        return self.newroot

    def dfs(self, root: TreeNode) -> None:
        if root is None:
            return
        self.dfs(root.left)
        if self.newroot is None:
            tempNode = TreeNode(root.val, None, None)
            self.newroot = tempNode
            self.current = tempNode
        else:
            tempNode = TreeNode(root.val, None, None)
            self.current.right = tempNode
            self.current = self.current.right

        self.dfs(root.right)
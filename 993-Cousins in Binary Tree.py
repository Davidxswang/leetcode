"""
https://leetcode.com/problems/cousins-in-binary-tree/
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

# time complexity: O(n), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xparent, xlayer = self.findParent(root, x, 0)
        yparent, ylayer = self.findParent(root, y, 0)
        if xlayer == ylayer and xparent is not yparent:
            return True
        else:
            return False

    def findParent(self, root: TreeNode, number: int, layer: int) -> TreeNode:
        if root.left is None and root.right is None:
            return None, None
        if root.left and root.left.val == number or root.right and root.right.val == number:
            return root, layer
        if root.left:
            left, leftlayer = self.findParent(root.left, number, layer + 1)
        else:
            left, leftlayer = None, None
        if root.right:
            right, rightlayer = self.findParent(root.right, number, layer + 1)
        else:
            right, rightlayer = None, None
        return (left, leftlayer) if left is not None else (right, rightlayer)

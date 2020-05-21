"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

# Thanks for the solution by @bindloss in discussion area.
# The trick here is to traverse a binary search tree in order. When doing so, the same element will be consecutive.
# time complexity: O(n), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.prev = None
        self.max = 0
        self.result = []
        self.current_count = 0
        self.dfs(root)
        return self.result

    def dfs(self, root: TreeNode) -> None:
        if root is None:
            return
        self.dfs(root.left)
        self.current_count = 1 if root.val != self.prev else self.current_count + 1

        if self.current_count > self.max:
            self.max = self.current_count
            self.result = [root.val]
        elif self.current_count == self.max:
            self.result.append(root.val)
        self.prev = root.val
        self.dfs(root.right)

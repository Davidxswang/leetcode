"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.



Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
"""

# time complexity: O(n), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root, 0)
        return self.result

    def dfs(self, root: TreeNode, prev: int) -> None:
        if root.left is None and root.right is None:
            self.result += prev * 2 + root.val
        if root.left is not None:
            self.dfs(root.left, prev * 2 + root.val)
        if root.right is not None:
            self.dfs(root.right, prev * 2 + root.val)
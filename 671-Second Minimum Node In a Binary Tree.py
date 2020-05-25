"""
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:

Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""

# I didn't come up with this solution. Thanks for the solution provided by the problem.
# So the basic idea is
# - The global minimum is root.val for sure.
# - If we find another one larger than minimum, it's the potential answer.
# - If we find a node that is equal to or larger than the potential answer, than we don't need to check the left and right substree of this node, because this node is the smallest of that subtree.
# - If we find a node that is smaller than the potential answer (surely larger than the global min), we need to replace the potential answer by this number and we don't need to check its left and right subtrees. Reason same as above.
# - If we find a node that is equal to the global minimum, we need to traverse its left and right subtrees because we might find better potential answer in the subtrees.
# time complexity: O(n), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.min = root.val
        self.answer = float('inf')
        self.dfs(root)

        return self.answer if self.answer < float('inf') else -1

    def dfs(self, root: TreeNode) -> None:
        if root:
            if self.min < root.val < self.answer:
                self.answer = root.val
            elif root.val == self.min:
                self.dfs(root.left)
                self.dfs(root.right)
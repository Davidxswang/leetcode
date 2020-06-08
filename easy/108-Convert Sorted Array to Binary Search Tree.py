"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Easy to code but hard to think it out. Every time, take in the lower and upper bound.
# Put the middle element in the root and recursively build the left and right subtree of the root.
# time complexity: O(n), space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], left: int, right: int) -> TreeNode:
        if right - left < 0:
            return None

        middle = left + (right - left) // 2
        node = TreeNode(nums[middle])
        node.left = self.build(nums, left, middle - 1)
        node.right = self.build(nums, middle + 1, right)

        return node

# This is inspired by one of the solutions in the discussion area. If the upper bound is inclusive, like len(nums) instead of len(nums) -1,
# then the base case would be if right - right == 0: return None
# one can use len(nums) == 0 to test if the base case holds.
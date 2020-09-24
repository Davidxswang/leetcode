"""
https://leetcode.com/problems/house-robber-iii/
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""

# time complexity: O(n), space complexity: O(n) where n is the number of nodes in the tree
# two solutions are both provided by @fun4LeetCode in the discussion area.
# the first is dynamic programming solution, and the second is greedy bottom-up solution.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    """dp solution
    def rob(self, root: TreeNode) -> int:
        return self.subrob(root, dict())
    
    def subrob(self, root, record):
        if root is None:
            return 0
        if root in record:
            return record[root]
        
        value = root.val
        if root.left:
            value += self.subrob(root.left.left, record) + self.subrob(root.left.right, record)
        
        if root.right:
            value += self.subrob(root.right.left, record) + self.subrob(root.right.right, record)
        
        result = max(value, self.subrob(root.left, record) + self.subrob(root.right, record))
        record[root] = result
        
        return result
    """
    
    # bottom up
    def rob(self, root: TreeNode) -> int:
        robroot, notrobroot = self.subrob(root)
        return max(robroot, notrobroot)
    
    def subrob(self, root):
        if root is None:
            return 0, 0
        
        robleft, notrobleft = self.subrob(root.left)
        robright, notrobright = self.subrob(root.right)
        
        robroot = root.val + notrobleft + notrobright
        notrobroot = max(robleft, notrobleft) + max(robright, notrobright)
        
        return robroot, notrobroot
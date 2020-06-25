"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

0 <= n <= 8
"""

# time complexity: O(n!), space complexity: O(n)
# we set each number to root, and figure out how many kinds of left subtrees and right subtrees there are, we multiply them together to get the final answer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        result = []
        for i in range(1, n+1):
            leftnodes = self.getTree(1, i-1)
            rightnodes = self.getTree(i+1, n)
            for left in leftnodes:
                for right in rightnodes:
                    result.append(TreeNode(i, left, right))
        return result
    
    def getTree(self, start: int, end: int) -> List[TreeNode]:
        if start > end:
            return [None]
        elif start == end:
            return [TreeNode(start)]
        else:
            result = []
            for i in range(start, end+1):
                leftnodes = self.getTree(start, i-1)
                rightnodes = self.getTree(i+1, end)
                for left in leftnodes:
                    for right in rightnodes:
                        result.append(TreeNode(i, left, right))
        return result

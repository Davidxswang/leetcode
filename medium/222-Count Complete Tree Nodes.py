"""
https://leetcode.com/problems/count-complete-tree-nodes/
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# time complexity: O(n), space complexity: O(n)
# we could take advantage the quality of the complete binary tree, but it's trivial to save the time complexity

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        counter = 0
        from collections import deque
        queue = deque([root])
        while queue:
            node = queue.popleft()
            counter += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return counter

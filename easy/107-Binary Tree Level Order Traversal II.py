"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# It's pretty simple, go through each level and make a list for them and then add this list in the first position of final result list
# time complexity: O(n), space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            levelresult = []
            length = len(queue)
            for i in range(length):
                if queue[i] is not None:
                    levelresult.append(queue[i].val)
            result.insert(0,levelresult)
            for i in range(length):
                node = queue.pop(0)
                if node is None:
                    continue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return result
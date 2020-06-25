"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# time complexity: O(n), space complexity: O(n)
# I used two stacks here for clarity, one stores the layer that we should read from left to right and the other stores the layer that we should read from right to left and we just need to pay attention to what order we should follow when we put in the left and right children into the stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = [[]]
        stack_toright = [root]
        stack_toleft = []
        toright = True
        size = 1
        while stack_toright or stack_toleft:
            node = stack_toright.pop() if toright else stack_toleft.pop()
            size -= 1
            if node:
                result[-1].append(node.val)
                if toright:
                    if node.left:
                        stack_toleft.append(node.left)
                    if node.right:
                        stack_toleft.append(node.right)
                else:
                    if node.right:
                        stack_toright.append(node.right)
                    if node.left:
                        stack_toright.append(node.left)
            if size == 0 and (stack_toright or stack_toleft):
                size = len(stack_toright) + len(stack_toleft)
                result.append([])
                toright = not toright
        if result and not result[-1]:
            result.pop()
        return result

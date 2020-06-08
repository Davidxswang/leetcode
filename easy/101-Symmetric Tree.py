"""
https://leetcode.com/problems/symmetric-tree/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""

# This is the iterative way. Pretend there are two trees, we were gonna compare if these two trees are symmetric.
# Use a queue to store the nodes from two trees. Each time, pop 2 nodes from the front of the queue and compare.
# If they are the same, then add the left leaf of the left node, right leaf of the right tree, right leaf of the left tree,
# left leaf of the right tree into the tail of the queue consecutively.
# time complexity: O(n), space complexity: O(width of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]
        while queue:
            node_1 = queue.pop(0)
            node_2 = queue.pop(0)
            if node_1 is None and node_2 is None:
                continue
            if node_1 is None or node_2 is None or node_1.val != node_2.val:
                return False
            else:
                queue.extend([node_1.left,node_2.right,node_1.right,node_2.left])
        return True

# here since we pop(0) which is the first element in the queue, this is a breadth first search (BFS)
# if we change the pop(0) to pop() which is the last element of the stack, this is a depth first search (DPS)
# in DPS, the time complexity: O(n), space complexity: O(height of the tree)




# This is the recursive way. Very tricky but super simple.
# time complexity: O(n), space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, left, right) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
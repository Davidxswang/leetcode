"""
https://leetcode.com/problems/binary-tree-paths/
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# time complexity: O(n), space complexity: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.result = list()
        prefix = ""
        self.writePath(root, prefix)
        return self.result

    def writePath(self, root: TreeNode, prefix: str) -> None:
        if root is None:
            return

        prefix += "->" + str(root.val)
        if root.left is None and root.right is None:
            self.result.append(prefix[2:])
            return
        if root.right is not None:
            self.writePath(root.right, prefix)
        if root.left is not None:
            self.writePath(root.left, prefix)

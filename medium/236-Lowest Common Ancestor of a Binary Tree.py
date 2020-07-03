"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""

# the two solutions are provided by the solution set of the question.
# the code and algorithms are very elegant.

# time complexity: O(n), space complexity: O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
# the main idea of the first algorithm is to find the moment when p and q are spread in node, node.left and node.right, so that node+left+right>=2

        """
        recursive
        if not root:
            return None
        if root.val == q.val or root.val == p.val:
            return root
        
        self.answer = None
        
        def recurse_tree(node):
            if node is None:
                return False
            
            if node.val == p.val or node.val == q.val:
                mid = True
            else:
                mid = False
            
            left = recurse_tree(node.left)
            right= recurse_tree(node.right)
            
            if mid + left + right >= 2:
                self.answer = node
            
            return left or mid or right
        
        recurse_tree(root)
        return self.answer
        """
        
# the second algorithm is to traverse the tree until both q and p are found
# when we traverse, we mark down the parent of each node we have visited
# Then we from p using the parent notes, find the path to root
# at last, we start from q and go back to root, see when we will find the same node in p's path, that will be the lowest common ancestor        
        stack = [root]
        parent = {root:None}
        
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        
        p_parents = set()
        while p:
            p_parents.add(p)
            p = parent[p]
        
        while q not in p_parents:
            q = parent[q]
        
        return q

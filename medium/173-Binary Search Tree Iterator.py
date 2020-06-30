"""
https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""

# time complexity: O(1) averagely, space complexity: O(height of the tree)
# the key here is to make sure we finish the left traversal of the node in the stack.
# The solution of this problem is more concise.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        if root:
            self.stack = [root]
        else:
            self.stack = []
        while self.stack and self.stack[-1].left:
            node = self.stack[-1].left
            self.stack[-1].left = None
            self.stack.append(node)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """

        while self.stack and self.stack[-1].left:
            node = self.stack[-1].left
            self.stack[-1].left = None
            self.stack.append(node)
        
        node = self.stack.pop()
        if not node.left and not node.right:
            return node.val
        if node.right:
            self.stack.append(node.right)
            return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return not not self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

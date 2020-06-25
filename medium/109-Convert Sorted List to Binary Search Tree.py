"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

# These three solutions are all provided by the solution of this question, among which I think the third solution is the most interesting one.

# we can just each time break the list into halves, and recursively build the tree on these two halves.
# be careful with the case where head is the only node in the list
# time complexity: O(nlogn), space complexity: O(logn)
    """
    solution 1, 208ms
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        middle = self.findMiddle(head)
        if middle is head:
            return TreeNode(middle.val)
        else:
            return TreeNode(middle.val, self.sortedListToBST(head), self.sortedListToBST(middle.next))
    
    def findMiddle(self, head: ListNode) -> ListNode:
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        if prev:
            prev.next = None
        
        return slow
    """

# we can convert the linked list to an array and trade space for time, because the time we spend on finding the middle node in array is constant
# time complexity: O(n), space complexity: O(n)    

    """
    solution 2, 124ms
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        def convert(start, end):
            if start == end:
                return TreeNode(values[start])
            if start > end:
                return None
            mid = start + (end-start)//2
            return TreeNode(values[mid], convert(start, mid-1), convert(mid+1, end))
        
        return convert(0, len(values)-1)
    """
    
# This is the most interesting version of the solution.
# We can build a balanced binary search tree from a single sorted linked list.
# the way we do it is that we pretend we can find the middle element but we don't really find it. Instead, we recursively cut the list into half, and run on the left half to find the left node, then make the root node using the current head, then move the head to the next linked node, run do the same thing on right half and connect it to the right node of the root.
# this question's webpage has a vivid example for you to look at, it's so brilliant.

    """
    solution 3, 168ms
    
    def getSize(self, head) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size = self.getSize(head)
        
        def convert(start, end):
            nonlocal head
            if start > end:
                return None
            
            mid = start + (end-start) // 2
            
            left = convert(start, mid-1)
            
            node = TreeNode(head.val)
            node.left = left
            
            head = head.next
            
            node.right = convert(mid+1, end)
            return node
        
        return convert(0, size-1)
    """

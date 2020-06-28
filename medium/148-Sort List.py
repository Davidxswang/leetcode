"""
https://leetcode.com/problems/sort-list/
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# time complexity: O(nlogn), space complexity: O(1)
# This question is very good. The key here is to use a step to control the bucket manually. When we split, we cut two small pieces with length "step" from the list and merge them together; when we merge, we connect them two together and connect it to the formaly finished the tail, and return the tail of the finished list this time.
# Very genious solution.
# This solution is inspired by @zdwu in the discussion area.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getSize(self, head: ListNode) -> int:
        i = 0
        while head:
            i += 1
            head = head.next
        return i
    
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        step = 1
        size = self.getSize(head)
        newhead = ListNode(0, head)
        while step < size:
            cur = newhead.next
            tail = newhead      # the tail or last merge
            while cur:
                leftstart = cur
                rightstart = self.split(leftstart, step)
                cur = self.split(rightstart, step)
                tail = self.merge(leftstart, rightstart, tail)
            step *= 2
        return newhead.next
    
    
    def split(self, left: ListNode, step: int) -> ListNode:
        i = 1
        while i < step and left:
            i += 1
            left = left.next
        if not left:
            return None
        right = left.next
        left.next = None
        return right
    
    
    def merge(self, left: ListNode, right: ListNode, head: ListNode) -> ListNode:
        cur = head

        while left and right:
            if left.val > right.val:
                cur.next = right
                right = right.next
                cur = cur.next
            else:
                cur.next = left
                left = left.next
                cur = cur.next
        
        cur.next = left if left else right
        while cur.next:
            cur = cur.next
        return cur
                

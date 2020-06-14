"""
https://leetcode.com/problems/swap-nodes-in-pairs/
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# time complexity: O(n), space complexity: O(1)
# this problem is interesting, we need three pointers to track the previous pointer, and two current pointers. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = newhead = ListNode(0, head)
        p1 = head
        p2 = head.next
        while p1 and p2:
            # before: prev -> p1 -> p2 -> post
            # after:  prev -> p2 -> p1 -> post
            post = p2.next
            prev.next = p2
            p2.next = p1
            p1.next = post
            
            # move to the next
            # either we have two or more node:
            #   before: prev -> p2 -> p1 -> post
            #   after:                prev -> p1 -> p2
            # or we only have 1 node left:
            #   in this case, we should stop
            prev = p1
            p1 = post
            if p1:
                p2 = p1.next
            else:
                return newhead.next
        return newhead.next
        

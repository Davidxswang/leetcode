"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# time complexity: O(n), space complexity: O(1)
# this solves this problem in one pass.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        final = head
        i = 1
        while i <= n:
            final = final.next
            i += 1
        if final is None:
            return head.next
        while True:
            if final.next is None:
                p.next = p.next.next
                return head
            else:
                p = p.next
                final = final.next

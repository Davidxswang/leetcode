"""
https://leetcode.com/problems/reorder-list/
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# time complexity: O(n), space complexity: O(n)
# Double end queue really helps in this question.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        from collections import deque
        queue = deque()
        p = head
        while p:
            queue.append(p)
            p = p.next
        
        popfromleft = True
        prev = None
        while queue:
            node = queue.popleft() if popfromleft else queue.pop()
            if not prev:
                prev = node
            else:
                prev.next = node
                prev = prev.next
            popfromleft = not popfromleft
        prev.next = None

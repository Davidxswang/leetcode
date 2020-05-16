"""
https://leetcode.com/problems/reverse-linked-list/
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Iterative method.
# Always be careful with the first node. The first node's next should be None.
# time complexity: O(n), space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        p1 = head
        p2 = head.next
        while p2 and p1:
            if p1 == head:
                p1.next = None
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        return p1

# Recursive method. Inspired by the solution provided by the problem set.
# time complexity: O(n), space complexity: O(n) due to the function call stack
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
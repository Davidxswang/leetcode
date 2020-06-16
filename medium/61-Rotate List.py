"""
https://leetcode.com/problems/rotate-list/

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

"""

# time complexity: O(n), space complexity: O(1)
# the key idea here is to use two pointers separated at k distance and move them together to find the right final node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        k %= length
        if k == 0:
            return head
        newfinal = head
        newfinal_kdis = head
        while k > 0:
            newfinal_kdis = newfinal_kdis.next
            k -= 1
        while newfinal_kdis.next:
            newfinal_kdis = newfinal_kdis.next
            newfinal = newfinal.next
        newhead = newfinal.next
        newfinal_kdis.next = head
        newfinal.next = None
        return newhead 

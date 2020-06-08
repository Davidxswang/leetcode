"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

# pretty simple one. If this one is the same as the next one, just next one (by making point.next = point.next.next)
# time complexity: O(n), space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        point = head
        while point and point.next:
            if point.val == point.next.val:
                point.next = point.next.next
            else:
                point = point.next
        return head
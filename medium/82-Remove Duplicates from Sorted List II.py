"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

# time complexity: O(n), space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newhead = prev = ListNode(0, head)
        p = head
        while p and p.next:
            if p.val != p.next.val:
                prev, p = p, p.next
            else:
                temp = p.val
                while p and p.val == temp:
                    p = p.next
                if p is None:
                    prev.next = None
                    return newhead.next
                else:
                    prev.next = p
        return newhead.next

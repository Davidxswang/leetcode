"""
https://leetcode.com/problems/remove-linked-list-elements/
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Pretty easy.
# time complexity: O(n), space complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val == val:
            head = head.next
        if head is not None:
            pointer = head
        else:
            return None
        while pointer is not None:
            if pointer.next is None:
                return head
            else:
                if pointer.next.val == val:
                    pointer.next = pointer.next.next
                else:
                    pointer = pointer.next
        return head
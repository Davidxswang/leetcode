"""
https://leetcode.com/problems/partition-list/
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# time complexity: O(n), space complexity: O(1)
# The idea is to build two lists, one for <x and the other for >=x, then connect them together


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        p = head.next
        if head.val >= x:
            largeprev, largehead = head, head
            smallprev, smallhead = None, None
        else:
            smallprev, smallhead = head, head
            largeprev, largehead = None, None
        head.next = None
        while p:
            if p.val >= x:
                if largeprev:
                    largeprev.next = p
                    largeprev = largeprev.next
                else:
                    largehead, largeprev = p, p
                p = p.next
                largeprev.next = None
            else:
                if smallprev:
                    smallprev.next = p
                    smallprev = smallprev.next
                else:
                    smallhead, smallprev = p, p
                p = p.next
                smallprev.next = None
        if smallprev:
            smallprev.next = largehead
        return smallhead if smallhead else largehead

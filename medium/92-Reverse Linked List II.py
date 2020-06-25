"""
https://leetcode.com/problems/reverse-linked-list-ii/
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# time complexity: O(n), space complexity: O(1)
# the main idea is to:
#   - find the m-1 node
#   - reverse the m-n node
#   - connect m-1 node with n node and m node with n+1 node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        counter = 1
        p = head
        prev = newhead = ListNode(0, head)
        while counter < m:
            counter += 1
            p = p.next
            prev = prev.next
        # counter == m, p is m-th node
        pprev = None
        tail = p
        while counter <= n:
            pnext = p.next
            p.next = pprev
            pprev = p
            p = pnext
            counter += 1
        prev.next = pprev
        tail.next = p
    
        return newhead.next

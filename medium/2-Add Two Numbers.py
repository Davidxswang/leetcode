"""
https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# time complexit: O(n), space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = p1 = l1
        p2 = l2
        
        addone = 0
        while p1 or p2 or addone:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            digit = val1 + val2 + addone
            digit, addone = (digit, 0) if digit <= 9 else (digit%10, 1)
            if not p1 and not p2:
                prev.next = ListNode(digit)
            else:
                if p1 and p2:
                    prev = p1
                    p1.val = digit
                    p1 = p1.next
                    p2 = p2.next
                elif p1:
                    prev = p1
                    p1.val = digit
                    p1 = p1.next
                else:
                    prev.next = p2
                    prev = p2
                    p2.val = digit
                    p2 = p2.next

        return head

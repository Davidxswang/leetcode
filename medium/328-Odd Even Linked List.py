"""
https://leetcode.com/problems/odd-even-linked-list/
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
 

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
"""

# time complexity: O(n), space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        i = 1
        odd = ListNode()
        even = ListNode()
        p_odd = odd
        p_even = even
        
        p = head
        
        while p:
            p_next = p.next
            if i % 2 == 1:
                p_odd.next = p
                p.next = None
                p_odd = p_odd.next
                i += 1
            else:
                p_even.next = p
                p.next = None
                p_even = p_even.next
                i += 1
            p = p_next
        
        if even.next:
            p_odd.next = even.next
        
        return odd.next
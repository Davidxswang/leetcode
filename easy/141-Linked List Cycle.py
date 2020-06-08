"""
https://leetcode.com/problems/linked-list-cycle/
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.




Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""


# Pretty easy. This is the most prevalent method, double pointers: slow pointer and fast pointer.
# Since if there is a loop, the fast pointer will run faster than the slow pointer and will catch up from the back of slow pointer.
# They will eventually meet at some point.
# time complexity: O(n), space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
                if fast == slow:
                    return True
            else:
                return False


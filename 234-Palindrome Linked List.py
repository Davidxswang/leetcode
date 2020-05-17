"""
https://leetcode.com/problems/palindrome-linked-list/
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# I didn't come up with the solution. This is inspired by @yavinci in the discussion area.
# Use slow and fast pointer to find the middle+1 element. If 6, it's 4, if 5, it's 4.
# Then reverse the second half, e.g. if 6, reverse 4-6, if 5, reverse 4-5.
# Compare the element one by one on the first and second half.
# time complexity: O(n), space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # if there are odd number of elements: e.g. 5, the fast will stop at the last element, slow=3, fast = 5
        # if there are even number of elements: e.g. 6, the fast will stop at the None, slow=4, fast=None(after 6)

        if fast is not None:
            slow = slow.next
        # this will take effect when the number of elements is odd, e.g. 5, slow=4, fast=5
        # this can ensure the second half is shorter

        slow = self.reverse(slow)

        while slow is not None:
            if head.val == slow.val:
                head = head.next
                slow = slow.next
            else:
                return False

        return True

    def reverse(self, slow: ListNode) -> None:
        prev = None
        while slow is not None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        return prev
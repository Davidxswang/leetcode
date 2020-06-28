"""
https://leetcode.com/problems/linked-list-cycle-ii/
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow-up:
Can you solve it without using extra space?
"""

# Using extra space: using a set to remember what we have seen when we go through, if we find a node that is pointing to a node we have seen, the node being pointed is the node we are looking for.
# time complexity: O(n), space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        p = head
        while p:
            if p.next in visited:
                return p.next
            visited.add(p)
            p = p.next
        return None


# second solution:
# this is inspired by @Dico in the discussion area and the video on YouTube: https://www.youtube.com/watch?time_continue=2&v=zbozWoMgKW0
# Actually this solution utilizes Floyd's Algorithm to detect the loop:
# - use slow and fast two pointers to go through the linked list, the speed is 1 and 2 respectively. If they never meet, there is no loop in the linked list
# - if slow and fast pointers meet at some time, there is a loop, now we need to find the start point of the loop:
#   - let's use q and p pointing to head and the node where slow and fast meet, let them move 1 step forward each time, when they meet, they meet at the start node of the loop.
# time complexity: O(n), space complexity: O(1)
# but this time complexity should be larger than the first one since the slow and fast pointer may loop through the loop more than once.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # there is a loop
                p = head
                q = slow
                while p is not q:
                    q = q.next
                    p = p.next
                return p
        return None

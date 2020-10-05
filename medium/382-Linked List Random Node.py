"""
https://leetcode.com/problems/linked-list-random-node/
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
"""

# time complexity: O(n), space complexity: O(1)
# Reservior Sampling: for every element at index i, generate an element from (0, 1) if it's smaller than 1/i, choose the element at index i
# every element should have the same probability to be chosen, e.g.,
# the last element to be chosen: 1/n
# the second to the last element to be chosen: 1/(n-1) * (n-1)/n = 1/n
# ...
# the key here is that even if an element might be chosen in the current step, it is still possible for the element to be replaced by the following elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        import random
        current = self.head
        counter = 1
        choice = current
        
        while current is not None:
            if random.random() < 1/counter:
                choice = current
            current = current.next
            counter += 1
        
        return choice.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""

# time complexity: O(n), space complexity: O(1)
# Both solutions are provided by me. The first one didn't use a prev counter to record the last node in this layer. So it has to traverse more than once.
# the second one use a prev pointer which allows the program just traverse every node once.



"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    """
    solution 1, 48ms
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while root:
            cur = root
            while cur:
                if cur.left:
                    if cur.right:
                        cur.left.next = cur.right
                    else:
                        p = cur.next
                        while p and not p.left and not p.right:
                            p = p.next
                        if p:
                            cur.left.next = p.left if p.left else p.right
                        else:
                            cur.left.next = None
                if cur.right:
                    p = cur.next
                    while p and not p.left and not p.right:
                        p = p.next
                    if p:
                        cur.right.next = p.left if p.left else p.right
                    else:
                        cur.right.next = None
                cur = cur.next
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                p = root.next
                while p and not p.left and not p.right:
                    p = p.next
                if p:
                    root = p.left if p.left else p.right
                else:
                    root = None
        return head
    """
    
    
    """
    solution 2, 64ms
    """
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while root:
            prev = None
            cur = root
            nextroot = None
            while cur:
                if cur.left:
                    if not prev:
                        prev = cur.left
                        nextroot = cur.left
                    else:
                        prev.next = cur.left
                        prev = prev.next
                if cur.right:
                    if not prev:
                        prev = cur.right
                        nextroot = cur.right
                    else:
                        prev.next = cur.right
                        prev = prev.next
                cur = cur.next
            root = nextroot
        return head

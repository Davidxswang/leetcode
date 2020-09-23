"""
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false
"""

# time complexity: O(n), space complexity: O(n)
# the key is to treat [k, #, #] as a valid binary tree and represent it as # recursively
# if the only a # is left in the end, it's a valid b-tree

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        nodes = preorder.split(',')
        
        if not nodes:
            return False
        
        while nodes:
            node = nodes.pop(0)
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append('#')
        
        if len(stack) == 1 and stack[0] == '#':
            return True
        return False
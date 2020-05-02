"""
https://leetcode.com/problems/valid-parentheses/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


# the core is to use a stack to trace the pair-state of the parentheses
# push the first one into the stack
# if seeing a closing parentheses, we should be able to pop out the opening immediately
# time complexity: O(n), space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        dic = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        if s == None or len(s) == 0:
            return True
        for i in range(len(s)):
            if i == 0:
                stack.append(s[i])
            else:
                if s[i] in dic:
                    if len(stack) != 0 and stack[-1] == dic[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(s[i])
        if len(stack) == 0:
            return True
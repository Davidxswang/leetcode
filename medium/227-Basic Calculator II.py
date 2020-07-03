"""
https://leetcode.com/problems/basic-calculator-ii/
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

# time complexity: O(n), space complexity: O(n)


class Solution:
    def calculate(self, s: str) -> int:
        from collections import deque
        
        queue = deque()
        
        i = 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                if queue and queue[-1] not in ('+', '-'):
                    queue[-1] = queue[-1] * 10 + int(s[i])
                else:
                    queue.append(int(s[i]))
            elif s[i] in ('*', '/'):
                op1 = queue.pop()
                j = i+1
                op2 = 0
                while j < len(s) and s[j] not in ('+', '-', '*', '/'):
                    if s[j] != ' ':
                        op2 = op2*10 + int(s[j])
                    j += 1
                if s[i] == '*':
                    queue.append(op1 * op2)
                else:
                    queue.append(op1 // op2)
                i = j-1
            elif s[i] in ('+', '-'):
                queue.append(s[i])
            i += 1
        
        
        while len(queue) > 1:
            op1, op, op2 = queue.popleft(), queue.popleft(), queue.popleft()
            if op == '+':
                queue.appendleft(op1 + op2)
            else:
                queue.appendleft(op1 - op2)
        
        return queue[0]
        

"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

# time complexity: O(n), space complexity: O(n)
# the key is to use a stack to store the operands and result of the operation, when we meed the operator, we take out two operands to operate on. When we finish the operation, we store the result in the stack.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
            op = tokens[i]
            if op in ('+','-','*','/'):
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if op == '+':
                    stack.append(op1 + op2)
                elif op == '-':
                    stack.append(op1 - op2)
                elif op == '*':
                    stack.append(op1 * op2)
                else:
                    if op2 * op1 < 0 and op1 % op2 != 0:
                        stack.append(op1 // op2 + 1)
                    else:
                        stack.append(op1 // op2)
            else:
                stack.append(op)
            i += 1
        return stack[-1] if stack else 0
            

"""
https://leetcode.com/problems/different-ways-to-add-parentheses/

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""

# time complexity: O((2n-2)!/(n-1)!/(n-1)!/n), space complexity: O(n), where n is the number of numbers in the string
# the solution is inspired by @2guotou in the discussion area. The time complexity is inspired by @tianyuHHH in the comment under this post. The proof is here: http://people.math.sc.edu/howard/Classes/554b/catalan.pdf
# this is a very genious way to solve this problem. We should see this problem bottom up:
# if two numbers are in the string, one way to calculate it, f(2) = 1 
# if three numbers are in the string, two way to calculate it, f(3) = 2
# if four numbers are in the string, f(1)*f(3)+f(2)*f(2)+f(3)*f(1) to calculate it
# so the solution is just a top-down method of calculating it. 

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input:
            return []
        
        result = []
        
        def calculate(op1, op2, op3):
            if op2 == '+':
                return op1 + op3
            if op2 == '-':
                return op1 - op3
            if op2 == '*':
                return op1 * op3
        
        for i in range(len(input)):
            if input[i] in ('+', '-', '*'):
                leftlist = self.diffWaysToCompute(input[:i])
                rightlist = self.diffWaysToCompute(input[i+1:])
                result += [calculate(left, input[i], right) for left in leftlist
                                                            for right in rightlist]
        if not result:
            result = [int(input)]
            
        return result

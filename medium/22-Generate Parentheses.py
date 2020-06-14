"""
https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
# time complexity: O(2^(2n)), space complexity: O(2n), the time complexity is due to the number of solutions, we basically traverse every solution, even though the number of solution is less than 2^(2n), the space complexity is due to the call stack.
# this is inspired by @brobins9 in the dicussion area.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.recursive(result, '', 0, 0, n)
        return result
    
    def recursive(self, result: List[str], base: str, opennum: int, closenum: int, total: int) -> None:
        if len(base) == 2*total:
            result.append(base)
            return
        
        if opennum < total:
            self.recursive(result, base+'(', opennum+1, closenum, total)
        
        if closenum < opennum:
            self.recursive(result, base+')', opennum, closenum+1, total)

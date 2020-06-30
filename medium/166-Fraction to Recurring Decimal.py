"""
https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""

# time complexity: O(hard to estimate), space complexity: O(hard to estimate)
# this solution is inspired by @tusizi in the discussion area.
# It's not that hard, it's just not easy integrate all of these together in a concise way.

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '' if numerator * denominator >= 0 else '-'
        div, remainder = divmod(abs(numerator), abs(denominator))
        if remainder == 0:
            return sign+str(div)
        result = [sign+str(div)+'.']
        
        remainder_stack = []
        
        while remainder not in remainder_stack:
            remainder_stack.append(remainder)
            div, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(div))
        
        if not remainder:
            return (''.join(result))[:-1]
        
        index = remainder_stack.index(remainder)
        result.insert(index+1, '(')
        result.append(')')
        return ''.join(result)

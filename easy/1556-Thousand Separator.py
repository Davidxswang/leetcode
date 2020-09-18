"""
https://leetcode.com/problems/thousand-separator/
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"
 

Constraints:

0 <= n < 2^31
"""

# time complexity: O(logn), space complexity: O(logn) where n is the input n as an integer.

class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = str(n)
        
        result = []
        
        while len(num) > 3:
            result.append(num[-3:])
            num = num[:-3]
        
        if len(num) > 0:
            result.append(num)
        
        return '.'.join(result[::-1])

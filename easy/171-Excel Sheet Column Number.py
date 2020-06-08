"""
https://leetcode.com/problems/excel-sheet-column-number/
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

# Pretty easy.
# time complexity: O(n), space complexity: O(n)
class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum([ (ord(s[i])-ord('A')+1)*pow(26,len(s)-i-1) for i in range(len(s))]) if len(s) > 0 else 0

# Pretty easy.
# time complexity: O(n), space complexity: O(1)
class Solution:
    def titleToNumber(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result = 0
        for i in range(len(s)):
            result = result * 26 + (ord(s[i])-ord('A')+1)
        return result
"""
https://leetcode.com/problems/excel-sheet-column-title/
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""

# They trick part is that it starts from 1.
# time complexity: O(logn), space complexity: O(logn)
class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            result = chr((n-1) % 26 + ord('A')) + result
            n = (n-1) // 26
        return result
"""
https://leetcode.com/problems/add-strings/
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

# Pretty easy.
# time complexity: O(n+m), space complexity: O(max(m,n)), where m and n are the lengths of the two strings respectively.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        addone = 0
        for i in range(max(len(num1),len(num2))):
            if i >= len(num1):
                number1 = 0
                number2 = ord(num2[-1-i]) - ord('0')
            elif i >= len(num2):
                number1 = ord(num1[-1-i]) - ord('0')
                number2 = 0
            else:
                number1 = ord(num1[-1-i]) - ord('0')
                number2 = ord(num2[-1-i]) - ord('0')
            r = number1 + number2 + addone
            if r > 9:
                addone = 1
                r -= 10
            else:
                addone = 0
            result = str(r)+result
        if addone != 0:
            result = '1' + result
        return result
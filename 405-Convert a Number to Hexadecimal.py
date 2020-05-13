"""
https://leetcode.com/problems/convert-a-number-to-hexadecimal/
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
"""

# Pretty easy.
# time complexity: O(logn), space complexity: O(logn)
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        result = ""
        if num < 0:
            num = pow(2,32)+num
        while num > 0:
            r = num % 16
            if 0 <= r <= 9:
                result = str(r)+result
            else:
                result = chr(ord('a') + (r-10)) + result
            num //= 16
        return result
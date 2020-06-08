"""
https://leetcode.com/problems/add-binary/
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""


# similar to problem 66, add from right to the left. If addone == 1 at the end, add another digit in the front
# time complexity: O(n), space complexity:O(n), n is the length of the longer string in a and b
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlength = max(len(a), len(b)) * -1
        i = -1
        addone = 0
        result = ""
        while i >= maxlength:
            if i >= len(a) * -1:
                digit_a = 0 if a[i] == '0' else 1
            else:
                digit_a = 0
            if i >= len(b) * -1:
                digit_b = 0 if b[i] == '0' else 1
            else:
                digit_b = 0
            sumdigit = digit_a + digit_b + addone
            if sumdigit >= 2:
                sumdigit %= 2
                addone = 1
            else:
                addone = 0
            result = str(sumdigit) + result
            i -= 1
        if addone == 1:
            result = '1' + result
        return result
"""
https://leetcode.com/problems/to-lower-case/
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ''
        for s in str:
            if ord('A') <= ord(s) <= ord('Z'):
                result += chr(ord(s) - ord('A') + ord('a'))
            else:
                result += s
        return result
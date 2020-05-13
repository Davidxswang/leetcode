"""
https://leetcode.com/problems/number-of-segments-in-a-string/
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

# time complexity: O(n), space complexity: O(1)
class Solution:
    def countSegments(self, s: str) -> int:
        space = True
        result = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                space = True
            else:
                if s[i] != ' ' and space:
                    result += 1
                    space = False
            i += 1
        return result
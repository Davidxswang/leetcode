"""
https://leetcode.com/problems/length-of-last-word/
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


# check each letter of the string, if a non-space letter is found, check if the letter before it is a space
# if so, length starts from 1, if not, length is incremented
# this is very important when there is space at the end of the string like "Hello World     "
# time complexity: O(n), space complexity: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        length = 0
        i = 0
        space = False
        while i < len(s):
            if s[i] != ' ':
                if space == True:
                    length = 1
                    space = not space
                else:
                    length += 1
            else:
                space = True
            i += 1
        return length
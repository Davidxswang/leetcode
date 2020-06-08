"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

# time complexity: O(n), space complexity: O(1)
class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        s = list(s)
        start = None
        end = None
        while i < len(s):
            if s[i] != ' ' and start == None:
                start = i
            if i == len(s)-1 and s[i] != ' ' or i != len(s)-1 and s[i] != ' ' and s[i+1] == ' ':
                end = i
                while start is not None and end is not None and start < end:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                start = None
                end = None
            i += 1
        return ''.join(s)
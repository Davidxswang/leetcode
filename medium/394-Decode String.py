"""
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        from itertools import repeat
        
        stack = []
        
        number = 0
        data = ''
        for i, letter in enumerate(s):
            if letter == '[':
                continue
            elif letter == ']':
                letters, numbers = stack.pop(), stack.pop()
                if stack and isinstance(stack[-1], str): 
                    stack[-1] += ''.join(repeat(letters, numbers))
                else:
                    stack.append(''.join(repeat(letters, numbers)))
            elif '0' <= letter <= '9':
                number = number * 10 + int(letter)
                if s[i+1] == '[':
                    stack.append(number)
                    number = 0
            else:
                data += letter
                if i == len(s) - 1 or s[i+1] == ']' or '0' <= s[i+1] <= '9':
                    if stack and isinstance(stack[-1], str):
                        stack[-1] += data
                    else:
                        stack.append(data)
                    data = ''
        return ''.join(stack)
"""
https://leetcode.com/problems/reverse-vowels-of-a-string/
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

# Pretty easy.
# time complexity: O(n), space complexity: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        a = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        i, j = 0, len(s)-1
        while i < j:
            if s[i] in a and s[j] in a:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
            elif s[i] in a:
                j -= 1
            elif s[j] in a:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s)
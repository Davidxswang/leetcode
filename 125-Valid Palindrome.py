"""
https://leetcode.com/problems/valid-palindrome/
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

# Pretty easy.
# time complexity: O(n), space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        while i<j:
            if ord('a') <= ord(s[i]) <= ord('z') or ord('0') <= ord(s[i]) <= ord('9'):
                first = s[i]
            elif ord('A') <= ord(s[i]) <= ord('Z'):
                first = chr(ord(s[i]) - ord('A') + ord('a'))
            else:
                i += 1
                continue
            if ord('a') <= ord(s[j]) <= ord('z') or ord('0') <= ord(s[j]) <= ord('9'):
                second = s[j]
            elif ord('A') <= ord(s[j]) <= ord('Z'):
                second = chr(ord(s[j]) - ord('A') + ord('a'))
            else:
                j -= 1
                continue
            if first == second:
                i += 1
                j -= 1
            else:
                return False
        return True
"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

# time complexity: O(n^2), space complexity: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        result = s[0]
        # aba type
        for i in range(1, len(s)-1):
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result = result if right-left+1 <= len(result) else s[left:right+1]
                left -= 1
                right += 1
        for i in range(len(s)-1):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result = result if right-left+1 <= len(result) else s[left:right+1]
                left -= 1
                right += 1
        return result

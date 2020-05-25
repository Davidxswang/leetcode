"""
https://leetcode.com/problems/valid-palindrome-ii/
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


# I didn't come up with the solution. Thanks for the solution provided by the problem.
# The idea is very easy:
# Check from left and right toward the center, if there is a mismatch between s[i] and s[j] (for i < j)
# Then there has to be a palindrome either in s[i+1]-s[j] or in s[i]-s[j-1]
# time complexity: O(n), space complexity: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s, i, j - 1) or self.isPalindrome(s, i + 1, j)
            i += 1
            j -= 1
        return True

    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        i = start
        j = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
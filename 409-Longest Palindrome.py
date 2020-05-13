"""
https://leetcode.com/problems/longest-palindrome/
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

# Be careful with the case "ccc" or "ababa"
# The principle is to add all the even numbers and all the odd(>1)-1 numbers and plus one(if there is odd number)
# time complexity: O(n), space complexity: O(n)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        result = 0
        hasone = 0
        for letter in s:
            dic[letter] = 1 if letter not in dic else dic[letter]+1
        for value in dic.values():
            if value % 2 == 0:
                result += value
            else:
                result += value - 1
                hasone = 1
        result += hasone
        return result
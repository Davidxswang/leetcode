"""
https://leetcode.com/problems/valid-anagram/
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

# time complexity: O(n), space complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = dict()
        for i in s:
            dic[i] = 1 if i not in dic else dic[i]+1
        for i in t:
            if i not in dic or dic[i] == 0:
                return False
            else:
                dic[i] -= 1
        if sum(list(dic.values())) == 0:
            return True
        else:
            return False
"""
https://leetcode.com/problems/isomorphic-strings/
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

# Be careful we need to cross check to strings: from s to t and from t to s
# time complexity: O(n), space complexity: O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        i = 0
        dicst = {}
        dicts = {}
        while i in range(len(s)):
            if s[i] in dicst and t[i] in dicts:
                if dicst[s[i]] != t[i] or dicts[t[i]] != s[i]:
                    return False
                else:
                    i += 1
            elif s[i] not in dicst and t[i] not in dicts:
                dicst[s[i]] = t[i]
                dicts[t[i]] = s[i]
            else:
                return False

        return True
"""
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

# Pretty easy.
# time complexity: O(n), space complexity: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                dic[s[i]] = -1
        position = len(s)
        values = dic.values()
        for i in values:
            if 0 <= i < position:
                position = i
        return -1 if position == len(s) else position
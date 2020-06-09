"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# time complexity: O(n), space complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        result = 0
        i = 0
        j = 1
        temp = set()
        temp.add(s[i])
        while j < len(s):
            if s[j] not in temp:
                temp.add(s[j])
                j += 1
                result = max(len(temp), result)
            else:
                result = max(len(temp), result)
                while s[i] != s[j]:
                    temp -= {s[i]}
                    i += 1
                i += 1
                j += 1
        return result
                
            

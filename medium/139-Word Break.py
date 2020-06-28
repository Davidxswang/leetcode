"""
https://leetcode.com/problems/word-break/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

# time complexity: O(n^2), space complexity: O(n)
# this is inspired by @segfault in the discussion area.
# Using DP, the problem can be solved in an array.
# - If the s[0:i+1] in word array, location i is good
# - If not, look from i to 0 (let's say j), see if j is good and s[j+1:i+1] is in word array, if so, i is good; if not, i is bad.
# - When we finish, return whether n-1 is good or not.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)
        flag = [False] * len(s)
        for i in range(0, len(s)):
            if s[:i+1] in dic:
                flag[i] = True
                continue
            for j in range(i-1, -1, -1):
                if flag[j] and s[j+1:i+1] in dic:
                    flag[i] = True
                    break
        return flag[-1]
            


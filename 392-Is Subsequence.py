"""
https://leetcode.com/problems/is-subsequence/
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""


# Kind of tricky.
# time complexity: O(m+n), space complexity: O(1), where m and n are the lengths of the string s and t respectively.
# if there are lots of incoming S, I should store S using a hashing table. When new S comes, I should check if this new S is a subsquence of the stored hash table, If so, it must be a subsquence of t.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0
        pointer_t = 0
        while pointer_s < len(s):
            while pointer_t < len(t):
                if t[pointer_t] == s[pointer_s]:
                    pointer_t += 1
                    pointer_s += 1
                    break
                else:
                    pointer_t += 1
            if pointer_t == len(t) and pointer_s < len(s):
                return False
        if pointer_s == len(s):
            return True
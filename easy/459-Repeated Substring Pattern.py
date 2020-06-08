"""
https://leetcode.com/problems/repeated-substring-pattern/
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

# My solution, pretty easy.
# time complexity: O(n^(1.5)), space complexity: O(1)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 1
        while i < len(s):
            if len(s) % i != 0:
                i += 1
                continue
            j = i
            while j < len(s):
                if s[j] == s[j%i]:
                    j += 1
                else:
                    break
            i += 1
            if j == len(s):
                return True
        return False

# The best solution I found in the discussion area is by @rsrs3.
    def repeatedSubstringPattern(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1

# this is based on the fact that if str = SaSa or more(SaSaSa, SaSaSaSa, ....), then two str together: strstr but with 1 and last letter removed,
# will become: SxSaSaSy, or more(SxSaSaSaSaSy, SxSaSaSaSaSaSaSy, ...), then when using strstr.find(str), this new string should contain the original string.
# This is brilliant!
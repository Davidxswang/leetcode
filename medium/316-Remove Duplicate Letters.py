"""
https://leetcode.com/problems/remove-duplicate-letters/

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "cdadabcc"
Output: "adbc"
Example 2:

Input: s = "abcd"
Output: "abcd"
Example 3:

Input: s = "ecbacba"
Output: "eacb"
Example 4:

Input: s = "leetcode"
Output: "letcod"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

"""

# time complexity: O(26*n), space complexity: O(26*n) where n is the length of s
# the solution is inspired by @lixx2100 in the forum.
# the idea is to deal with the unique letters in current string s one-by-one, if we find a letter that after its first appearance, all the unique letters appear, we append the result by this letter and delete this letter from the rest of the string to its right, and the current string becomes its right part

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for letter in sorted(set(s)):
            suffix = s[s.index(letter):]
            if set(suffix) == set(s):
                return letter + self.removeDuplicateLetters(suffix.replace(letter, ''))
        
        return ''
"""
https://leetcode.com/problems/reverse-only-letters/
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        i = 0
        j = len(s) - 1
        while i < j:
            if ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z') and ('a' <= s[j] <= 'z' or 'A' <= s[j] <= 'Z'):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if not ('a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z'):
                i += 1
            if not ('a' <= s[j] <= 'z' or 'A' <= s[j] <= 'Z'):
                j -= 1

        return ''.join(s)
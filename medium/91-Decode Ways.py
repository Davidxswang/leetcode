"""
https://leetcode.com/problems/decode-ways/
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

# time complexity: O(n), space complexity: O(1)
# I tried recursion, but the time complexity is too large
# then I choose this linear algorithm
# the main idea is to use two separate vars to store the result of current element either as a standalone number or as a follow-up element of the previous number
# finnally, add these vars together

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        onlyone = 1
        withfront = 0
        i = 1
        while i < len(s):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    onlyone, withfront = 0, onlyone
                else:
                    return 0
            elif s[i-1] == '1':
                onlyone, withfront = onlyone+withfront, onlyone
            elif s[i-1] == '2':
                if 1 <= int(s[i]) <= 6:
                    onlyone, withfront = onlyone+withfront, onlyone
                else:
                    onlyone, withfront = onlyone+withfront, 0
            else: # 3-9
                onlyone, withfront = onlyone+withfront, 0
            i += 1
        return onlyone+withfront

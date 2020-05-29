"""
https://leetcode.com/problems/shortest-distance-to-a-character/
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        left = [0] * len(S)
        right = [0] * len(S)
        for i in range(len(S)):
            if S[i] == C:
                left[i] = 0
            elif i != 0:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 10001

            if S[~i] == C:
                right[~i] = 0
            elif ~i != -1:
                right[~i] = right[~i + 1] + 1
            else:
                right[~i] = 10001

        result = []
        for i in range(len(S)):
            result.append(min(left[i], right[i]))

        return result
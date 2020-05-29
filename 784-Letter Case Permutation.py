"""
https://leetcode.com/problems/letter-case-permutation/
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

# time complexity: O(2^n), space complexity: O(n), where n is the number of letters in the string S

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        data = dict()
        result = []
        S = list(S)
        index = 0
        for i in range(len(S)):
            if 'a' <= S[i] <= 'z':
                data[index] = (i, S[i], chr(ord(S[i]) - ord('a') + ord('A')))
                index += 1
            elif 'A' <= S[i] <= 'Z':
                data[index] = (i, S[i], chr(ord(S[i]) - ord('A') + ord('a')))
                index += 1

        for i in range(2 ** len(data)):
            chosen = self.decode(i, len(data))
            for j in range(len(chosen)):
                S[data[j][0]] = data[j][chosen[j] + 1]
            result.append(''.join(S))

        return result

    def decode(self, number: int, length: int):
        result = []
        while length >= 1:
            result.insert(0, number & 1)
            number = number >> 1
            length -= 1
        return result



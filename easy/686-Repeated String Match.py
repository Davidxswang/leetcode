"""
https://leetcode.com/problems/repeated-string-match/
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""

# time complexity: O(n), space complexity: O(n), where n is the length of B

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if len(B) % len(A) == 0:
            start = len(B) // len(A)
        else:
            start = len(B) // len(A) + 1

        if (A * start).find(B) >= 0:
            return start
        elif (A * (start + 1)).find(B) >= 0:
            return start + 1
        else:
            return -1
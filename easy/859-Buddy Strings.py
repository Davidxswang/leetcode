"""
https://leetcode.com/problems/buddy-strings/
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) < 2:
            return False
        prev = -1
        A = list(A)
        B = list(B)
        dic = dict()
        for i in range(len(A)):
            dic[A[i]] = dic.get(A[i], 0) + 1
            if A[i] != B[i]:
                if prev == -1:
                    prev = i
                else:
                    A[i], A[prev] = A[prev], A[i]
                    return A == B
        if prev == -1:
            for i in list(dic.keys()):
                if dic[i] > 1:
                    return True
            return False
        else:
            return False
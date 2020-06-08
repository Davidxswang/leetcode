"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""

# time complexity: O(n+m), space complexity: O(m+n) where n and m are the lengths of A and B

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dic = dict()
        i = 0
        word = ''
        while i < len(A):
            if A[i] == ' ':
                word = ''
            else:
                word += A[i]
                if i == len(A) - 1 or A[i + 1] == ' ':
                    dic[word] = dic.get(word, 0) + 1
                    word = ''
            i += 1

        i = 0
        word = ''
        while i < len(B):
            if B[i] == ' ':
                word = ''
            else:
                word += B[i]
                if i == len(B) - 1 or B[i + 1] == ' ':
                    dic[word] = dic.get(word, 0) + 1
                    word = ''
            i += 1

        return list(key for key in list(dic.keys()) if dic[key] == 1)

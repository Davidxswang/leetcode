"""
https://leetcode.com/problems/find-common-characters/
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

# time complexity: O(n), space complexity: O(1), where n is the number of letters in A

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        freq = [10001] * 26
        for word in A:
            flag = [0] * 26
            for letter in word:
                i = ord(letter) - ord('a')
                flag[i] += 1
            for i in range(len(flag)):
                freq[i] = min(flag[i], freq[i])
        result = []
        for i in range(len(freq)):
            while freq[i] > 0:
                result.append(chr(i + ord('a')))
                freq[i] -= 1
        return result
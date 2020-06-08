"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""

# time complexity: O(n), space complexity: O(m), where n and m are the lengths of words and chars respectively.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        dic = dict()
        for letter in chars:
            dic[letter] = dic.get(letter, 0) + 1
        import copy
        for word in words:
            temp = copy.copy(dic)
            okay = True
            for letter in word:
                if letter in temp and temp[letter] > 0:
                    temp[letter] -= 1
                else:
                    okay = False
                    break
            if okay:
                result += len(word)
        return result

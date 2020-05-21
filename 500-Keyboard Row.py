"""
https://leetcode.com/problems/keyboard-row/
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]


Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

# time complexity: O(n), space complexity: O(1), where n is the total length of all the words in words list.
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            word = words[i]
            if len(word) == 0:
                result.append(word)
            else:
                j = 0
                while j < len(word):
                    if self.row(word[j]) != self.row(word[0]):
                        break
                    j += 1
                if j == len(word):
                    result.append(word)
        return result

    def row(self, letter: str):
        keyboard = ['qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM']
        for i in range(len(keyboard)):
            if letter in keyboard[i]:
                return i
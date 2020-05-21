"""
https://leetcode.com/problems/detect-capital/
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.


Example 1:

Input: "USA"
Output: True


Example 2:

Input: "FlaG"
Output: False


Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

# time complexity: O(n), space complexity: O(1)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if len(word) == 2:
            if ord('A') <= ord(word[0]) <= ord('Z'):
                return True
            elif ord('a') <= ord(word[1]) <= ord('z'):
                return True
            else:
                return False
        # len == 3
        if ord('A') <= ord(word[0]) <= ord('Z'):
            i = 1
            while i < len(word):
                if ord('A') <= ord(word[i]) <= ord('Z') and ord('A') <= ord(word[1]) <= ord('Z') or ord('a') <= ord(
                        word[i]) <= ord('z') and ord('a') <= ord(word[1]) <= ord('z'):
                    i += 1
                else:
                    return False
            if i == len(word):
                return True
        else:
            i = 1
            while i < len(word):
                if ord('a') <= ord(word[i]) <= ord('z'):
                    i += 1
                else:
                    return False
            if i == len(word):
                return True

"""
https://leetcode.com/problems/word-pattern/
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""

# time complexity: O(n+m), space complexity: O(n+m) where n and m are the lengths of patter and str
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dicps = dict()
        dicsp = dict()
        word = ""
        i = -1
        j = 0
        while j in range(len(str)):
            if j == len(str) - 1 and str[j] != ' ' or j < len(str) - 1 and str[j] != ' ' and str[j + 1] == ' ':
                # an ending to a word
                word += str[j]
                i += 1
                if i >= len(pattern):
                    return False
                if pattern[i] in dicps and word in dicsp:
                    if dicps[pattern[i]] == word and dicsp[word] == pattern[i]:
                        j += 1
                        word = ''
                        continue
                    else:
                        return False
                elif pattern[i] not in dicps and word not in dicsp:
                    dicps[pattern[i]] = word
                    dicsp[word] = pattern[i]
                    j += 1
                    word = ''
                    continue
                else:
                    return False
            if str[j] == ' ':
                j += 1
                word = ''
            else:
                word += str[j]
                j += 1
        if i == len(pattern) - 1:
            return True
        else:
            return False

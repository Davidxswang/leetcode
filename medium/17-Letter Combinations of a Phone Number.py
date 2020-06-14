"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

# time complexity: O(3^n * 4^m), space complexity: O(1), where n is the number of number '2' to '8' and m is the number of number '9'
# this is a very good example of recursion.


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = []
        dic = { '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
              }
        
        def recurse(base: str, digit: str) -> None:
            if len(digit) == 0:
                result.append(base)
                return
            letter = digit[0]
            for i in range(len(dic[letter])):
                recurse(base+dic[letter][i], digit[1:])
        
        recurse('', digits)
        return result

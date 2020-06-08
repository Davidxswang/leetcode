"""
https://leetcode.com/problems/roman-to-integer/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# we can process it digit by digit, translate every digit to an integer and put them in the list, then sum them up
# if we see s[i]==s[i-1], increment the last element in the list, if we see s[i]<s[i-1], append another element to it
# if we see s[i]>s[i-1], we need to do some trick things to the last element of the list
# time complexity: O(n), space complexity: O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        result = []
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in range(len(s)):
            if i == 0:
                result.append(dic[s[i]])
            else:
                if dic[s[i]] < dic[s[i-1]]:
                    result.append(dic[s[i]])
                elif dic[s[i]] == dic[s[i-1]]:
                    result[-1] += dic[s[i]]
                else:
                    result[-1] = -1*result[-1] + dic[s[i]]
        return sum(result)

# to save some space, we can use a int to save the result directly, and get rid of the intermediate list
# time complexity: O(n), space complexity: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        i = 0
        while i < len(s):
            if i == len(s)-1:
                total += dic[s[i]]
                break
            if dic[s[i]] >= dic[s[i+1]]:
                total += dic[s[i]]
                i += 1
            else:
                total += dic[s[i+1]] - dic[s[i]]
                i += 2
        return total
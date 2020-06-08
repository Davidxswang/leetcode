"""
https://leetcode.com/problems/base-7/
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
"""


# time complexity: O(logn), space complexity: O(1)
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        result = ''
        sign = ''
        if num < 0:
            num = -num
            sign = '-'
        while num > 0:
            result = str (num % 7) + result
            num //= 7
        result = sign + result
        return result
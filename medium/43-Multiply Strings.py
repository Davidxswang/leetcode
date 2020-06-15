"""
https://leetcode.com/problems/multiply-strings/
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

# time complexity: O(m*n), space complexity: O(m+n), where m and n are the lengths of num1 and num2
# I didn't come up with the idea, this is inspired by @yavinci in the discussion area. The idea is to multiply each digit of num1 by each digit of num2 and put them in the right place in the result string. Then sum all the numbers in the same spot in the result string.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        result = [0] * (len(num1) + len(num2))
        # two digits * two digits could result in three digits or four digits
        
        for i in range(-1, -len(num1)-1, -1):
            for j in range(-1, -len(num2)-1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                low = digit1 * digit2 % 10
                high = digit1 * digit2 // 10
                result[i+j+1] += low
                result[i+j] += high
        
        for i in range(-1, -len(result)-1, -1):
            if result[i] >= 10:
                result[i-1] += result[i] // 10
                result[i] %= 10
            result[i] = str(result[i])
        
        return ''.join(result) if result[0] != '0' else ''.join(result[1:])

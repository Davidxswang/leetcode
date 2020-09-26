"""
https://leetcode.com/problems/count-numbers-with-unique-digits/
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
 

Constraints:

0 <= n <= 8
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        if n == 1:
            return 10
        
        result = 10
        
        # n >= 2, counter 2-digit till n-digit number
        count = 9 * 9
        for i in range(2, n+1):
            result += count
            count *= (9-(i-1))
        
        return result
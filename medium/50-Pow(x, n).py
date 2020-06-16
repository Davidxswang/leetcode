"""
https://leetcode.com/problems/powx-n/
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

# time complexity: O(log(n)), space complexity: O(1)
# the idea is very similar to question 29: divide two integers 

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        n_is_positive = n > 0
        n = abs(n)
        result = 1.0
        while n > 0:
            temp, i = x, 1
            while i <= n:
                result *= temp
                n -= i
                temp = temp*temp
                i *= 2
        
        return result if n_is_positive else 1/result

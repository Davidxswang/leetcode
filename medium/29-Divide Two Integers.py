"""
https://leetcode.com/problems/divide-two-integers/
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


"""

# time complexity: O(log(m/n)), space complexity: O(1), where m and n are dividend and divisor
# I didn't come up with this solution. This is inspired by @tusizi in the discussion area. This is very concise and elegant. Every time we subtract a divisor*(2^i) from dividend and if we succeed, we add this 2^i to the result. We do it again and again until the dividend is smaller than divisor.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0
        
        sign = (dividend > 0) is (divisor > 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1
                
        result = result if sign else -result
        
        return min(pow(2,31)-1, max(-pow(2,31), result))

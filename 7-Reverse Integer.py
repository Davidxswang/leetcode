"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


# python doesn't really have a limit for int, so the following method doesn't really comply with the requirement above.
# time complexity: log10(n), space complexity: 1
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        y = 0
        sign = 1 if x > 0 else -1
        x = x * sign
        while x > 0:
            y = y*10 + x%10
            x //= 10
        if y < 0:
            return 0
        y *= sign
        if y<=pow(2,31)-1 and y>=-1*pow(2,31):
            return y
        else:
            return 0


# to make it really comply with the requirement above, we need to let the program exit before it overflows
# if y overflows, then it happens when y= y*10+x%10, then before it happens, y must be >= (pow(2,31)-1-x%10)/10
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        y = 0
        sign = 1 if x > 0 else -1
        x = x * sign
        maxint = (pow(2,31)-1)
        while x > 0:
            if y >= (maxint-x%10)/10:
                return 0
            y = y*10 + x%10
            x //= 10
        return y*sign
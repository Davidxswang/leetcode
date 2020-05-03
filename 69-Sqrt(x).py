"""
https://leetcode.com/problems/sqrtx/
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""

# use divide-by-2 to narrow down the search interval
# time complexity: O(logn,based 2), space complexity: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 1
        right = x-1
        while left <= right:
            middle = left + (right - left) // 2
            if middle * middle <= x and (middle+1)*(middle+1) > x:
                return middle
            if middle * middle > x:
                right = middle
            else:
                left = middle

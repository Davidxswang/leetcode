"""
https://leetcode.com/problems/sum-of-square-numbers/
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:

Input: 3
Output: False
"""

# time complexity: O(n^0.5), space complexity: O(1)

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        import math
        i = 0
        j = int(math.sqrt(c))+1
        while i <= j:
            if i*i + j*j < c:
                i += 1
                continue
            if i*i + j*j > c:
                j -= 1
                continue
            if i*i + j*j == c:
                return True
        return False
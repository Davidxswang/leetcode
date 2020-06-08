"""
https://leetcode.com/problems/valid-perfect-square/
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""


# Pretty easy.
# time complexity: O(logn), space complexity: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        i,j = 1, num - 1
        while i < j:
            middle = i + (j - i) // 2
            if middle * middle > num:
                j = middle - 1
            elif middle * middle < num:
                i = middle + 1
            else:
                return True
            if i*i == num or j*j == num:
                return True
        return False
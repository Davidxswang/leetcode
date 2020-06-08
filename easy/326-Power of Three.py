"""
https://leetcode.com/problems/power-of-three/
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

# The question asks if we can do it without any loop or recursion, for Python it cannot.
# time complexity: O(logn), space complexity: O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n >= 2:
            mode = n % 3
            if mode != 0:
                return False
            n = n // 3
        return True
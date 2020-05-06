"""
https://leetcode.com/problems/power-of-four/
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""

# Inspired by @h285zhao in the discussion panel. If the number is a power of 4, then it in binary format should look like:
# 100 00000000000(number of 0 after 100 should be even).
# time complexity: O(logn) for the base conversion, space complexity: O(n)
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        s = bin(num)[3:]
        return num > 0 and ('1' not in s) and len(s)%2 == 0
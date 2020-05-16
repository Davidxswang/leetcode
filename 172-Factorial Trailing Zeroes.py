"""
https://leetcode.com/problems/factorial-trailing-zeroes/
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""

# I didn't come up with this solution. Thanks to @xcv58 in the discussion area.
# The trailing zeros depend on the number of 5 in n! because there are way more 2s than 5s in n!.
# To calculate the number of 5 in n!, we need to calculate there are how many numbers in n! containing:
# 5, like: 5, 10, 15, 20, 25, 30, 35...
# 25, like 25, 50
# 125, like 125, 250
# ...
# Take a close look, we can see if the number is like 5, 10, 15, 20, 55, 65, even though they are greater than 5, they only contain one 5
# But for numbers like 25, 50, they contain two 5s, i.e. they have 25 in them.
# Therefore, we need to calculate iteratively.
# time complexity: O(logn), space complexity: O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <= 4:
            return 0
        result = 0
        while n >= 5:
            result += n // 5
            n = n // 5
        return result
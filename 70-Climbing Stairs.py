"""
https://leetcode.com/problems/climbing-stairs/
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# using dynamic programming, f(n) = f(n-1) + f(n-2) because you can only climb 1 or 2 stairs each step
# time complexity: O(n), space complexity: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev_1 = 1
        prev_2 = 2
        result = 0
        i = 3
        while i <= n:
            result = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = result
            i += 1
        return result
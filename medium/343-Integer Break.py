"""
https://leetcode.com/problems/integer-break/
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""

# time complexity: O(n), space complexity: O(1)
# the solution is provided by @Chuqi in the discussion area. The math behind it is:
# if there is a factor f >= 4, then 2(f-2) = 2f-4 >= f, so factor 2 and 3 are preferred since 1 is waste.
# the strategy will be: if n > 4, we should factor out 3 out of n, if n == 4, we should factor out 4 itself since 2*2 > 1*3.
# the analysis is provided by @StefanPochmann and @lixx2100 in the discusssion area.

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        result = 1
        while n > 4:
            result *= 3
            n -= 3
        result *= n
        return result
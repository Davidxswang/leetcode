"""
https://leetcode.com/problems/single-number-ii/

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""


# time complexity: O(n), space complexity: O(1)
# This is a very brilliant solution provided by @felixhao28 in the discussion area.
# The main idea is to find a way to filter the result of those "normal" values. The way we do this is to modulo, the modular should have the same value with those normal frequency. @felixhao28 has a very good explanation using commutative and circular properties.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1<<i) != 0:
                    count[i] = (count[i] + 1) % 3
        result = sum(count[i]*pow(2,i) for i in range(32))
        
        if result >= pow(2,31):
            result -= pow(2,32)
        return result

"""
https://leetcode.com/problems/single-number-iii/

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

# time complexity: O(n), space complexity: O(1)
# the solution is inspired by @zhiqing_xiao in the discussion area.
# the key here is to use one bit to separate the nums into two groups and use the xor(n1,n2) to find out the n1 in one group and n2 in the other group.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        xor = 0
        for num in nums:
            xor ^= num
        
        testbit = 1
        while testbit & xor == 0:
            testbit <<= 1
        
        
        xor_set = xor
        xor_unset = xor
        for num in nums:
            if testbit & num != 0:
                xor_set ^= num
            else:
                xor_unset ^= num
            
        return [xor_set, xor_unset]

"""
https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

# time complexity: O(n), space complexity: O(1)
# this solution is inspired by @mzchen in the discussion area. 
# Using dynamic programming, we can log the min and max at every position, representing the min and max we can get at every position.
# The trick here is when we meet a negative element, we should swap the min and max.
# At every position, we should choose to use the prior result (max or min) or not. If we don't use the prior result and we can get better result, then we should not use the prior result. 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = nums[0]
        tempmax = tempmin = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                tempmax,tempmin = tempmin, tempmax
            
            tempmax = max(tempmax*nums[i], nums[i])
            tempmin = min(tempmin*nums[i], nums[i])
        
            result = max(result, tempmax)
        
        return result

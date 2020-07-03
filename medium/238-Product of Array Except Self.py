"""
https://leetcode.com/problems/product-of-array-except-self/
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
# the first solution is provided by me, one traversal, two arrays, using dp.
# time complexity: O(n), space complexity: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[~i] = right[~i+1] * nums[~i+1]
        
        return [left[i]*right[i] for i in range(len(nums))]
        """
# the second solution is provided by the solution of this question
# time complexity: O(n), space complexity: O(1). space saved by using the final result as the temporary list for computation
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
        
        right = 1
        for i in range(len(nums)-2, -1, -1):
            right *= nums[i+1]
            result[i] *= right
        
        return result

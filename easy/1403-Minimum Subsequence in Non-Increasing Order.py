"""
https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

 

Example 1:

Input: nums = [4,3,10,9,8]
Output: [10,9] 
Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included, however, the subsequence [10,9] has the maximum total sum of its elements. 
Example 2:

Input: nums = [4,4,7,6,7]
Output: [7,7,6] 
Explanation: The subsequence [7,7] has the sum of its elements equal to 14 which is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6). Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions. Note the subsequence has to returned in non-decreasing order.  
Example 3:

Input: nums = [6]
Output: [6]
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 100
"""
# time complexity: O(nlogn), space complexity: O(n)

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        nums.sort(reverse=True)
        left = [0] * len(nums)
        right = [0] * len(nums)
        left[0] = nums[0]
        right[-1] = 0
        right[-2] = nums[-1]
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i]
            right[~i] = right[~i+1] + nums[~i+1]
        
        for i in range(len(nums)):
            if left[i] > right[i]:
                return nums[:i+1] 

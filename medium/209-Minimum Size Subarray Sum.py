"""
https://leetcode.com/problems/minimum-size-subarray-sum/
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        start = end = 0
        shortest = len(nums)+1
        tempsum = 0
        while end < len(nums):
            tempsum += nums[end]
            while tempsum >= s and start <= end:
                shortest = min(shortest, end-start+1)
                tempsum -= nums[start]
                start += 1
            if tempsum < s:
                start -= 1
                tempsum += nums[start]
            end += 1
        return shortest if shortest <= len(nums) else 0
                

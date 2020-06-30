"""
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Follow up: Your solution should be in logarithmic complexity.
"""

# time complexity: O(logn), space complexity: O(logn) due to the call stack
# The solution is provided by the solution set of the problem.
# The main idea here is to use a binary search algorithm to find a peak. Since we only need to find one peak, we can let the search range shrink 1/2 every time. 
# The shrink direction is the key. We should let it shrink to the direction where the middle element gets higher.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        return self.find(nums, 0, len(nums)-1)
    
    def find(self, nums: List[int], start: int, end: int) -> int:
        if start > end:
            return None
        if start == end:
            return start
        if end == len(nums) - 1 and nums[end-1] < nums[end]:
            return end
        mid = start + (end-start) // 2
        if nums[mid+1] > nums[mid]:
            return self.find(nums, mid+1, end)
        else:
            return self.find(nums, start, mid)
            

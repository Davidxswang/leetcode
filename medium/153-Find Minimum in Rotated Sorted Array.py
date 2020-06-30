"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

# time complexity: O(logn), space complexity: O(logn) due to the call stack

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        return self.find(nums, 0, len(nums)-1)
    
    def find(self, nums: List[int], start: int, end: int) -> int:
        if start > end:
            return None
        if nums[start+1] < nums[start]:
            return nums[start+1]
        if nums[end] < nums[end-1]:
            return nums[end]
        mid = start + (end-start) // 2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid] < nums[mid-1]:
            return nums[mid]
        else:
            if nums[mid] < nums[start]:
                return self.find(nums, start+1, mid-1)
            else:
                return self.find(nums, mid+1, end-1)

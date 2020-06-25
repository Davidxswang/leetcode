"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

"""

# time complexity: O(n), space complexity: O(n)
# because there are duplicate numbers and the list is rotated, so binary search is not very useful here, the worst case time complexity is O(n) because I used two searches with each call

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return self.find(nums, 0, len(nums)-1, target)
    
    def find(self, nums: List[int], start: int, end: int, target: int) -> bool:
        if start > end:
            return False
        if target == nums[start] or target == nums[end]:
            return True
        
        mid = start + (end-start) // 2
        if target == nums[mid]:
            return True
        
        return self.find(nums, start+1, mid-1, target) or self.find(nums, mid+1, end-1, target)
            
        

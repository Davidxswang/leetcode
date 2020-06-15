"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""

# time complexity: O(logn), space complexity: O(logn) due to the call stack.
# It's not hard, just be careful with the edge cases.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.findpos(nums, 0, len(nums)-1, target)
    
    def findpos(self, nums: List[int], start: int, end: int, target: int) -> int:
        if start > end:
            return -1
        if target == nums[start]:
            return start
        elif target == nums[end]:
            return end
        
        mid = start + (end-start) // 2
        belongtoleft = nums[mid] > nums[end]
        belongtoright = nums[mid] < nums[start]
        # Use these flags to see whether the middle element belongs to left subsequence or right subsequence

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            if belongtoleft or target < nums[end]:
                return self.findpos(nums, mid+1, end-1, target)
            else:
                return self.findpos(nums, start+1, mid-1, target)
        else: # target < nums[mid]
            if belongtoright or target > nums[start]:
                return self.findpos(nums, start+1, mid-1, target)
            else:
                return self.findpos(nums, mid+1, end-1, target)

"""
https://leetcode.com/problems/move-zeroes/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

# Double pointers: read and write pointers.
# time complexity: O(n), space complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 0
        while read < len(nums):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
            read += 1
        while write < len(nums):
            nums[write] = 0
            write += 1

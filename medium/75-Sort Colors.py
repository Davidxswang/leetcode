"""
https://leetcode.com/problems/sort-colors/
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

# time complexity: O(n), space complexity: O(1)
# This is provided by me. The main idea is to partition the nums into three region:zero, working zone, and two.
# At the beginning, find the last zero and first two, the working region is between them.
# then we need to distinguish each element in working zone:
#   - if 1: good, continue
#   - if 2: put it in front of "first two", then move the first two pointer forwardby one step, because we scan our working zone from left to right, we have not checked the element in front of this new first two element, so we need to move the first two pointer to the left if and only if its left is also a 2.
#   - if 0: we can swap it with lastzero+1, and move working zone pointer to the right by 1.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastzero = -1
        firsttwo = len(nums)
        
        while lastzero < len(nums)-1 and nums[lastzero+1] == 0:
            lastzero += 1
        
        while firsttwo > 0 and nums[firsttwo-1] == 2:
            firsttwo -= 1
        
        i = lastzero + 1
        while i < firsttwo:
            if nums[i] == 0:
                nums[i], nums[lastzero+1] = nums[lastzero+1], nums[i]
                lastzero += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[firsttwo-1] = nums[firsttwo-1], nums[i]
                while firsttwo > i and nums[firsttwo-1] == 2:
                    firsttwo -= 1
            else:
                i += 1

# Inspired by @girikuncoro in the discussion area.
# This is a Dutch partition problem.
# Refer to: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
# The partition is: red:[0:red], unclassified:[red:blue+1], blue:[blue+1:]
# So at the beginning red, white, blue = 0, 0, len(nums)-1
# then if we are still in the unclassified region, we need to check white pointer
#   - if 0: swap it with red and red++,white++
#   - if 1: white++
#   - if 2: swap it with unclassified(blue) and unclassified--
# time complexity: O(n), space complexity: O(1)

def sortColors(self, nums):
    red, white, blue = 0, 0, len(nums)-1
    
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1

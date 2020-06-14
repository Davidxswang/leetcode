"""
https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

# time complexity: O(n^2), space complexity: O(1)
# this is such a classic question and I got the inspiration from @christopherwu0529 in the discussion area. The idea is to first sort the nums in O(nlogn), then for each number in this list, two pointers go over the number after it.
# To make it faster, early stop if the fixed number is larger than 0, because there will be no way we can make the sum equal to 0.

class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                low = i + 1
                high = len(nums) - 1
                while low < high:
                    if nums[i] + nums[low] + nums[high] == 0:
                        result.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[i] + nums[low] + nums[high] < 0:
                        low += 1
                    else:
                        high -= 1
            i += 1
        return result

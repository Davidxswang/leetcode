"""
https://leetcode.com/problems/subsets-ii/
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


# time complexity: O(2^n), space complexity: O(n)
# because the recursion takes more time than sorting, so we sort the array first
# the main idea is to recursive, either with the element or without the element
# if we recurse with the element, than we need to jump to the next distinct element

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.recursive([], 0, nums)
        return self.result
    
    def recursive(self, temp: List[int], start: int, nums: List[int]) -> None:
        if start >= len(nums):
            self.result.append(temp)
            return
        i = start + 1
        while i < len(nums) and nums[i] == nums[start]:
            i += 1 
        self.recursive(temp, i, nums)
        self.recursive(temp + [nums[start]], start + 1, nums)
        

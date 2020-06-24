"""
https://leetcode.com/problems/subsets/
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# time complexity: O(2^n), space complexity: O(n), where n is the number of the elements in the set

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for number in range(0, pow(2,n)):
            i = 0
            temp = []
            while number > 0:
                remainder = number % 2
                if remainder == 1:
                    temp.append(nums[i])
                i += 1
                number //= 2
            result.append(temp)
        return result

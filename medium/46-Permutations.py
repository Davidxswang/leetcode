"""
https://leetcode.com/problems/permutations/
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

# time complexity: O(n!), space complexity: O(n^2) because the call stack depth is n and every call stack will store a copy of the rest of nums so the upper bound is n^2

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.recursive([], nums)
        return self.result
    
    def recursive(self, temp: List[int], nums: List[int]) -> None:
        if not nums:
            self.result.append(temp)
        for i in range(len(nums)):
            new = list(nums)
            new.remove(nums[i])
            self.recursive(temp+[nums[i]], new)

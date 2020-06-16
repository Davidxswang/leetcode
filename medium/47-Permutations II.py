"""
https://leetcode.com/problems/permutations-ii/
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

# time complexity: O(n!), space complexity: O(n)
# the key idea here is to not put the same element in the same spot twice

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.recursive([], nums)
        return self.result
    
    def recursive(self, temp: List[int], nums: List[int]) -> None:
        if not nums:
            self.result.append(temp)
            return
        numset = set(nums)
        for _,value in enumerate(numset):
            newnums = list(nums)
            newnums.remove(value)
            self.recursive(temp+[value], newnums)

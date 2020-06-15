"""
https://leetcode.com/problems/combination-sum/
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

# time complexity: O(2^n), space complexity: O(n) due to the call stack
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates.sort(reverse=True)
        self.recursive(candidates, 0, target, [])
        return self.result
    
    def recursive(self, candidates: List[int], start: int, target: int, temp: List[int]) -> None:
        if start > len(candidates) - 1:
            return
        if candidates[start] > target:
            self.recursive(candidates, start+1, target, [])
        else:
            total = sum(temp) + candidates[start]
            if total == target:
                # if we find one, we should add it to the result
                self.result.append(temp+[candidates[start]])
            elif total < target:
                # if current element can be added to the temp, we should try to add it to the array
                self.recursive(candidates, start, target, temp+[candidates[start]])
            # no matter if the total is equal or larger or smaller than the target, we should try not including current element and go to next element.
            self.recursive(candidates, start+1, target, temp)
